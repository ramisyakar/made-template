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

depression_df=load_data_from_internet_with_gzip('https://ec.europa.eu/eurostat/api/dissemination/sdmx/3.0/data/dataflow/ESTAT/hlth_ehis_mh1i/1.0/*.*.*.*.*.*.*?c[freq]=A&c[unit]=PC&c[hlth_pb]=DPR,DPR_MJR,DPR_OTH&c[quant_inc]=QU1,QU2,QU3,QU4,QU5&c[sex]=M,F&c[age]=Y15-19,Y15-24,Y15-29,Y15-64,Y18-24,Y18-44,Y18-64,Y_GE18,Y20-24,Y25-29,Y25-34,Y25-64,Y35-44,Y45-54,Y45-64,Y55-64,Y65-74,Y_GE65,Y_GE75&c[geo]=EU27_2020,EU28,BE,BG,CZ,DK,DE,EE,IE,EL,ES,FR,HR,IT,CY,LV,LT,LU,HU,MT,NL,AT,PL,PT,RO,SI,SK,FI,SE,IS,NO,UK,RS,TR&compress=true&format=csvdata&formatVersion=2.0&c[TIME_PERIOD]=2019,2014')
gdp_df=load_data_from_internet_with_gzip('https://ec.europa.eu/eurostat/api/dissemination/sdmx/3.0/data/dataflow/ESTAT/tipsau10/1.0/*.*.*.*?c[freq]=A&c[na_item]=B1GQ&c[unit]=CP_MNAC,CLV15_MNAC,CLV_PCH_PRE&c[geo]=EU27_2020,EA20,BE,BG,CZ,DK,DE,EE,IE,EL,ES,FR,HR,IT,CY,LV,LT,LU,HU,MT,NL,AT,PL,PT,RO,SI,SK,FI,SE&compress=true&format=csvdata&formatVersion=2.0&c[TIME_PERIOD]=2019,2014')

#dropping unnecessary columns
depression_drop_cols=['STRUCTURE','STRUCTURE_ID','freq','unit']
gdp_drop_cols=['STRUCTURE','STRUCTURE_ID','freq','na_item']

#dropping unnecesary columns
depression_df.drop(depression_drop_cols,axis=1,inplace=True)
gdp_df.drop(gdp_drop_cols,axis=1,inplace=True)

#merging two datasets
merged_df = pd.merge(gdp_df,depression_df,  how='inner', left_on=['geo','TIME_PERIOD'], right_on = ['geo','TIME_PERIOD'])


# Get the current working directory, It should be made-template
current_path = os.getcwd()

#create connection to data 
engine = sqlite3.connect(os.path.join(current_path, 'data/economic_depression.sqlite'))

#save data to data folder as a sql database
merged_df.to_sql('economic_depression',engine,if_exists='replace',index=False)
