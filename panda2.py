import pandas as pd

try:
    df = pd.read_excel('C:\ACCOUNTS\munka.xlsx')
    #df.info()
    #print(type(df))df['GyEv'].values > 2010
    #print(df[['Eredmeny', 'GyEv']])
    #print(type(df['Kezelo2']))
    #df.info()

    #szurt = df.loc[((df['Tipus'] != 'G4 RF1') & (df['Tipus'] !='G4 RF1-MM')) & (df['Eredmeny'] != 'Megfelelt')]
    #szurt = df.loc[((df['Tipus'] != 'G4 RF1-MM') & (df['Eredmeny'] != 'Megfelelt') & (df['Tipus'] != 'G4 RF1') & (df['Eredmeny'] != 'Megfelelt'))]
    #print(szurt)
#------------------------------------------------------
    #darabszám feltétel szerint                                
    #--SQL-ben így néz ki:-->  SELECT Kezelo, COUNT(*) FROM munka WHERE Eredmeny = 'Megfelelt' AND GyEv > 2012 GROUP BY Kezelo
    print(df.where((df['Eredmeny'] == 'Megfelelt') & (df['GyEv'] > 2012)).groupby('Kezelo')['Kezelo'].count())
    #print(df['Kezelo'].value_counts())
#-------------------------------------------------------
    #adatok szürése ~WHERE
    #print(df.loc[(df['Tipus'] == 'G4 RF1') | (df['Tipus'] =='G4 RF1-MM') & (df['Eredmeny'] == 'Megfelelt'), ['Tipus', 'Eredmeny', 'Kezelo']]) 
    #szurt = df.loc[((df['Tipus'] != 'G4 RF1') | (df['Tipus'] !='G4 RF1-MM')) & (df['Eredmeny'] == 'Megfelelt')]
    #print(szurt)
#-----------------------------------------------------------
    #rendezés darabszám értéke szerint
    #print(szurt['GyEv'].value_counts(sort=True,ascending=True))

    #rendezés év szerint
    #print(szurt[['GyEv']].sort_values('GyEv',ascending=False).value_counts(sort=False))

    #rendezés megadott tartományban
    #print(szurt.iloc[123:360,0:10].sort_values('Gyari_Szam',ascending=False))
#-----------------------------------------------------------

    #print(df.where((df['Eredmeny'] == 'Megfelelt') & (df['GyEv'] > 2012))['Eredmeny'])
    #sd = df.loc[(df['Eredmeny'] == 'Megfelelt') & (df['GyEv'] <= 2005)]
    #print(sd.iloc[0:5,0:3])
    #print(df.iloc[2022:2023,:])
#-----------------------------------------------------------
    #tartomány adatainak mentése tömbbe    
    # tomb = df.iloc[0:20,0:5].values
    # print(tomb[0])
    '''    j = 0
    for i in tomb:
          j = j + 1
          if j == 1:
            print(i)'''
except Exception as e:
       # eml.send_mail(to, "File Upload, Data extract error: ", f"Data extract error: File location {dir}" + str(e))
        print("Data extract error: " + str(e))


