import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
import mplfinance as mpf
import json

df = pd.read_json('Stock List.json') # data from database
symbollist = df['symbol'].unique()
# print(symbollist)
df2 = pd.read_csv('history.csv')
symbol=df2['symbol'][len(df2['symbol'])-1]
print(symbol)# just for testing. actual input from search extract input frm there
if symbol in symbollist:
    df_google = df[df['symbol'] == symbol].copy()
    df_google['date'] = pd.to_datetime(df_google['date'])
    wm = input("Enter week/ month") # selection from drop down
    types = int(input("1.OHLC\n2.Candle3.Hollow")) # take input from front end integrate with angular (input from select menu)
    ltype = ['ohlc','candle','hollow'] # just for testing
    if wm=='w':
        indate=pd.to_datetime(input("Enter start date")) # user input from front end
        df_google = df_google[df_google['date'] > indate] 
        df_google = df_google.set_index('date')
        if len(df_google>=7):
            mpf.plot(df_google[:7],style="yahoo",type=ltype[types-1], title=str(symbol)+" stock price")
        else:
            mpf.plot(df_google,style="yahoo",type=ltype[types-1],title=str(symbol)+" stock price")
    elif wm=='m':
        indate=pd.to_datetime(input("Enter start date"))
        df_google = df_google[df_google['date'] > indate]
        df_google = df_google.set_index('date')
        if len(df_google>=30):    
            mpf.plot(df_google[:30],style="yahoo",type=ltype[types-1],title=str(symbol)+" stock price") # add title also
        else:
            mpf.plot(df_google,style="yahoo",type=ltype[types-1],title=str(symbol)+" stock price")
    else:
        df_google = df_google.set_index('date')    
        mpf.plot(df_google,style="yahoo",type=ltype[types-1],title=str(symbol)+" stock price",savefig='templates/mypic.jpeg')
else:
    print("No data available try entering another symbol")