import datetime
from sqlalchemy import create_engine 
import pandas as pd
import pyodbc
import os

#pwd = os.environ['PGPASS']
pwd = os.environ['PGPASS']
uid = os.environ['PGUID']
port = "5432"
driver = "{ODBC Driver 17 for SQL Server}"
server = "DESKTOP-5Q30QEQ\SQLEXPRESS"
#DESKTOP-5Q30QEQ
#DESKTOP-5Q30QEQ\SQLEXPRESS
db = "AdventureWorks"
database = "AdventureWorksDW2019"   #<------Eztmeg nézni
#time_data = "01/01/1900 00:00:0.000"
#default_date = datetime.strptime(time_data,format_data)
def extract():
    try:
        src_conn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';DATABASE=' + database + ';UID=' + uid + ';PWD=' + pwd)
        '''src_cursor = src_conn.src_cursor()
        src_cursor.execute(""" SELECT t.name AS table_name FROM sys.tables t WHERE t.name IN ('DimProduct','DimProductSubcategory','DimProductSubcategory','DimProductCategory','DimSalesTerritory','FactInternetSales')""")
        src_tables = src_cursor.fetchall()
        for tbl in src_tables:
            df = pd.read_sql_query(f'select * FROM {tbl[0]}', src_conn)
            load(df, tbl[0])   '''

    except Exception as e:
        print("Data extract error: " + str(e))  

    finally:
        src_conn.close() 

def load(df, tbl):
    try:
        rows_imported = 0
        engine = create_engine(f'postgresql://{uid}:{pwd}@{server}:{port}/{db}')
        print(f'importing rows {rows_imported} to {rows_imported + len(df)}... ')
        # save df to postgres
        df.to_sql(f"stg_{tbl}", engine, if_exists='replace', index=False)
        rows_imported += len(df)
        # add elapsed time to final print out
        print("Data imported successful")

    except Exception as e:
        print("Data load error: " + str(e)) 
try:
    #call extract function
    extract()
except Exception as e:
    print("Error while extracting data: " + str(e))                     
