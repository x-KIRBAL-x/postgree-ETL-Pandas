#import datetime
from sqlalchemy import create_engine
from sqlalchemy.engine import URL 
import pandas as pd
import pyodbc
import os

pwd = os.environ['PGPASS']
uid = os.environ['PGUID']

port = "5432"
driver = "{ODBC Driver 17 for SQL Server}"
server = "DESKTOP-5Q30QEQ"
db = "AdventureWorks"
database = "AdventureWorksDW2019"
#time_data = "01/01/1900 00:00:0.000"
#default_date = datetime.strptime(time_data,format_data)
def extract():
    try:
        """ print(pwd)
        print(uid)
        print(database)
        print(server) """
        src_conn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + '\SQLEXPRESS' +  ';DATABASE=' + database + ';UID=' + uid + ';PWD=' + pwd + ';Trusted_Connection=yes')
        src_cursor = src_conn.cursor()
        src_cursor.execute(""" SELECT t.name AS table_name FROM sys.tables t WHERE t.name IN ('DimProduct','DimProductSubcategory','DimProductSubcategory','DimProductCategory','DimSalesTerritory','FactInternetSales')""")
        src_tables = src_cursor.fetchall()
        for tbl in src_tables:
            #print(tbl[0]) #tbl egy tömb aminek az első elemét kérem le a tbl[0]-el az aktuális for -ban nincs második eleme
            df = pd.read_sql_query(f'select * FROM {tbl[0]}', src_conn)
            load(df, tbl[0])

    except Exception as e:
        print("Data extract error: " + str(e))  

    finally:
        src_conn.close() 

def load(df, tbl):
    try:
        rows_imported = 0
        engine = create_engine(f'postgresql://{uid}:{pwd}@localhost:{port}/{db}')
        print(f'importing rows {rows_imported} to {rows_imported + len(df)}...  for table {tbl}')
        # save df to postgres
        df.to_sql(f"stg_{tbl}", engine, if_exists='replace', index=False, chunksize=100000)
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
