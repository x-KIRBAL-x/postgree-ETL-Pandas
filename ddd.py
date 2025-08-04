import os
from sqlalchemy import create_engine
import pandas as pd
import pyodbc
#import panda2

'''uid = os.environ['PGUID']
print(uid)
print(os.environ['PGPASS'])'''
#print(panda2.szurt.iloc[1:50,2:12])

szam1 = 15
def kulso():
    szam1 = 10
    def belsö():
        nonlocal szam1
        szam1 += 1 
        print(szam1)
    return belsö
    
f1 = kulso()
print(f1)
f1()

#----------------------------------------másik példa------------------------------

def op_factory(oper,num):
    def operation(value):
        if oper == '+':
            return value+num 
        if oper == '-':
            return value-num
        if oper == '**':
            return value**num
        if oper =='gyok':
            return value**(1/num)
    return operation

osszeg = op_factory('+',4)
kivon = op_factory('-',2)
negyzet = op_factory('**', 2)
gyoke = op_factory('gyok',2)

print(negyzet(3))
print(gyoke(8))