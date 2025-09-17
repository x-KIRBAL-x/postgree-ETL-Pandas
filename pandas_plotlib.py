#import needed libraries
from sqlalchemy import create_engine
import pyodbc
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sys
# this is imported from config folder
#import config.email as eml
import os

#get password from environmnet var
dir = r'\postgres\pandas_plot'
#to = 'youremail@domain.com'

#extract data from sql server
def extract():
    try:
        # starting directory
        directory = dir
        # iterate over files in the directory
        for filename in os.listdir(directory):
            #get filename without ext
            print(filename)
            file_wo_ext = os.path.splitext(filename)[0]
            print(file_wo_ext)
            # only process excel files
            if filename.endswith(".xlsx"):
                f = os.path.join(directory, filename)
                # checking if it is a file
                if os.path.isfile(f):
                    df = pd.read_excel(f)

        
        for x in df.index:
            if df.loc[x, 'Calories'] > 5000:
                df.loc[x, 'Calories'] = df.loc[x, 'Calories'] * 0.05

        df.plot()

        plt.show()

    except Exception as e:
       # eml.send_mail(to, "File Upload, Data extract error: ", f"Data extract error: File location {dir}" + str(e))
        print("Data extract error: " + str(e))

try:
    #call extract function
    df = extract()
except Exception as e:
    #eml.send_mail(to, "File Upload, Data extract error: ", f"Function call to file mapping, Data extract error: File location {dir}" + str(e))
    print("Error while extracting data: " + str(e))    