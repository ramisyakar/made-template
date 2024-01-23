import urllib.request
import zipfile
import pandas as pd
from sqlalchemy import BIGINT, FLOAT, TEXT
url = 'https://www.mowesta.com/data/measure/mowesta-dataset-20221107.zip'

zip_name = 'mowesta-dataset.zip'

urllib.request.urlretrieve(url, zip_name)

with zipfile.ZipFile(zip_name) as zip_file:
    data_file = 'data.csv'

    with zip_file.open(data_file) as data:
        df = pd.read_csv(data,sep=';',decimal=',',index_col=False,usecols=['Geraet', 'Hersteller', 'Model', 'Monat', 'Temperatur in °C (DWD)', 'Batterietemperatur in °C', 'Geraet aktiv'],)


df.columns=['Geraet', 'Hersteller', 'Model', 'Monat', 'Temperatur',
       'Batterietemperatur', 'Geraet aktiv']

df['Temperatur']=(df['Temperatur'] * 9/5) + 32
df['Batterietemperatur']=(df['Batterietemperatur'] * 9/5) + 32


df=df[df['Geraet']>0]
df=df[df.Monat.apply(lambda x: x in range(1, 13))]
df=df[df['Geraet aktiv'].apply(lambda x: x in ('Ja','Nein'))]


table_name = 'temperatures'
db_file = "temperatures.sqlite"
df.to_sql(table_name, f'sqlite:///{db_file}', if_exists='replace', index=False, dtype={
        'Geraet': BIGINT,
        'Hersteller': TEXT,
        'Model': TEXT,
        'Monat': BIGINT,
        'Temperatur': FLOAT,
        'Batterietemperatur': FLOAT,
        'Geraet aktiv': TEXT
    })