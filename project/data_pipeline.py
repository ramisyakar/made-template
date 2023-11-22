import pandas as pd
import sqlite3
import os



depression_df=pd.read_csv('https://raw.githubusercontent.com/ramisyakar/depression_data/main/depression_income_quantile.csv')
gdp_df=pd.read_csv('https://raw.githubusercontent.com/ramisyakar/depression_data/main/gdp_2.csv')

#unnecessary columns
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