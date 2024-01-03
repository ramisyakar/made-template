import sqlite3
import os
import pandas as pd
import gzip
import io
import requests

def load_data_from_internet_with_gzip(gzip_file_url):
    
        # Extract all files from the gzip
    response = requests.get(gzip_file_url)
    
    
    if response.status_code == 200:
    # Create a file-like object from the gz file content
        gzip_file_content = io.BytesIO(response.content)

        with gzip.open(gzip_file_content, 'rt') as f:
            # Get the list of file names in the gzip archive

                df = pd.read_csv(f)
    else:
        print(f"Failed to fetch the gzip file. Status code: {response.status_code}")            

    return df

def run_pipeline(depression_url,gdp_url):
    depression_df=load_data_from_internet_with_gzip(depression_url)
    gdp_df=load_data_from_internet_with_gzip(gdp_url)


    #eliminating countries which do not have both year data 2014,2019
    drop_countries=['BE', 'EU28', 'NL', 'RS', 'UK','EU27_2020']
    depression_df.drop(depression_df[depression_df["geo"].isin(drop_countries)].index,inplace=True)

    #eliminating ages which do not common for all countries
    drop_ages=['Y15-29','Y18-24','Y18-44','Y18-64','Y15-19','Y20-24','Y25-29','Y25-64']
    depression_df.drop(depression_df[depression_df["age"].isin(drop_ages)].index,inplace=True)

    #dropping "DPR" values because basically they are sum of DPR_MJR and DPR_OTH values
    depression_df.drop(depression_df[depression_df["hlth_pb"]=="DPR"].index,inplace=True)

    #changing income quantile values for better explanation
    depression_df["quant_inc"]=depression_df["quant_inc"].map({'QU1':'Poor', 'QU2':'Low', 'QU3':'Average', 'QU4':'Comfortable', 'QU5':'Rich'})

    #filling missing values by mean
    depression_df=depression_df.fillna(depression_df.OBS_VALUE.mean())

    #dropping unnecessary columns
    depression_drop_cols=['STRUCTURE','STRUCTURE_ID','freq','unit','OBS_FLAG']
    gdp_drop_cols=['STRUCTURE', 'STRUCTURE_ID', 'freq', 'na_item', 'ppp_cat', 'unit', 'OBS_FLAG']

    #dropping unnecesary columns
    depression_df.drop(depression_drop_cols,axis=1,inplace=True)
    gdp_df.drop(gdp_drop_cols,axis=1,inplace=True)

    #merging two datasets
    merged_df = pd.merge(gdp_df,depression_df,  how='inner', left_on=['geo','TIME_PERIOD'], right_on = ['geo','TIME_PERIOD'])

    #changing column names for better self explanation
    merged_df.columns=['country', 'year', 'purchase_power', 'depression_level', 'income_quantile', 'sex',
        'age', 'depression_percentage']


    # Get the current working directory, It should be made-template
    current_path = os.getcwd()

    #create connection to data 
    engine = sqlite3.connect(os.path.join(current_path, 'data/economic_depression.sqlite'))

    #save data to data folder as a sql database
    merged_df.to_sql('economic_depression',engine,if_exists='replace',index=False)
    return merged_df

if __name__ == '__main__':
    depression_url="https://ec.europa.eu/eurostat/api/dissemination/sdmx/3.0/data/dataflow/ESTAT/hlth_ehis_mh1i/1.0/*.*.*.*.*.*.*?c[freq]=A&c[unit]=PC&c[hlth_pb]=DPR,DPR_MJR,DPR_OTH&c[quant_inc]=QU1,QU2,QU4,QU5,QU3&c[sex]=M,F&c[age]=Y15-19,Y15-24,Y15-29,Y15-64,Y18-24,Y18-44,Y18-64,Y20-24,Y25-29,Y25-34,Y25-64,Y35-44,Y45-54,Y45-64,Y55-64,Y65-74&c[geo]=EU27_2020,EU28,BE,BG,CZ,DK,DE,EE,IE,EL,ES,FR,HR,IT,CY,LV,LT,LU,HU,MT,NL,AT,PL,PT,RO,SI,SK,FI,SE,IS,NO,UK,RS,TR&compress=true&format=csvdata&formatVersion=2.0&c[TIME_PERIOD]=2019,2014"
    gdp_url="https://ec.europa.eu/eurostat/api/dissemination/sdmx/3.0/data/dataflow/ESTAT/sdg_10_10/1.0/*.*.*.*.*?c[freq]=A&c[na_item]=EXP_PPS_EU27_2020_HAB&c[ppp_cat]=GDP&c[unit]=PC&c[geo]=EU27_2020,EU28,EU27_2007,EA20,EA19,BE,BG,CZ,DK,DE,EE,IE,EL,ES,FR,HR,IT,CY,LV,LT,LU,HU,MT,NL,AT,PL,PT,RO,SI,SK,FI,SE,IS,NO,CH,UK,BA,ME,MK,AL,RS,TR,US,JP&compress=true&format=csvdata&formatVersion=2.0&c[TIME_PERIOD]=2019,2014"
    run_pipeline(depression_url,gdp_url)