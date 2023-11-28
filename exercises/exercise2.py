
import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

url="https://download-data.deutschebahn.com/static/datasets/haltestellen/D_Bahnhof_2020_alle.CSV"
df=pd.read_csv(url,sep=";")

df.drop("Status",axis=1,inplace=True)

in_valid_Verkehr_indexes=df[(df["Verkehr"]!="RV")&(df["Verkehr"]!="nur DPN")&(df["Verkehr"]!="FV")].index

df.drop(in_valid_Verkehr_indexes,inplace=True)

df.Laenge=df.Laenge.apply(lambda x:x.replace(",","."))
df.Breite=df.Breite.apply(lambda x:x.replace(",","."))
df.Laenge=df.Laenge.astype(float)
df.Breite=df.Breite.astype(float)

in_valid_Laenge_indexes=df[(-90>df["Laenge"])|(df["Laenge"]>90)].index
in_valid_Breite_indexes=df[(-90>df["Breite"])|(df["Breite"]>90)].index

df.drop(in_valid_Laenge_indexes,inplace=True)
df.drop(in_valid_Breite_indexes,inplace=True)

def check_IFOPT_format(x):
  try:
    parts = x.split(':')
    if len(parts) == 3 or (len(parts) == 4 and parts[3].isdigit()):
      return parts[0].isalpha() and parts[1].isdigit() and parts[2].isdigit()
    else:
      return False
  except:
    return False

in_valid_IFOPT_indexes=df[df.IFOPT.apply(lambda x:check_IFOPT_format(x))==False].index

df.drop(in_valid_IFOPT_indexes,inplace=True)

df.dropna(inplace=True)

df=df.reset_index().drop("index",axis=1)

df=df.reset_index()



db_file = "trainstops.sqlite"

# Create an SQLite engine
engine = create_engine(f"sqlite:///{db_file}", echo=True)

# Define a SQLAlchemy Base
Base = declarative_base()

# Define the SQLAlchemy model class
class TrainStops(Base):
    __tablename__ = 'trainstops'
    index = Column(Integer, primary_key=True)
    EVA_NR = Column(Integer)
    DS100 = Column(String)
    IFOPT = Column(String)
    NAME=Column(String)
    Verkehr=Column(String)
    Laenge=Column(Float)
    Breite=Column(Float)
    Betreiber_Name=Column(String)
    Betreiber_Nr=Column(Float)

# Create the table in the SQLite database
Base.metadata.create_all(engine)

# Insert the DataFrame into the SQLite database table
df.to_sql('trainstops', con=engine, if_exists='replace', index=False)

























