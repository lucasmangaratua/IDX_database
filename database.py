import sqlite3
import sqlalchemy
import pandas as pd
import yfinance as yf
import datetime as dt
from sqlalchemy import insert
from pandas.tseries.offsets import MonthEnd

read_df = pd.read_csv ('/IDX_listed.csv')

read_df['code'] = read_df['code'].add('.JK')
df = pd.DataFrame(read_df, columns=['code', 'name'])

data = []
for ticker in df.code:
    data.append(yf.download(ticker).reset_index())

engine = sqlalchemy.create_engine('sqlite:///INA.db')

for frame, symbol in zip(data, df.code):
        frame.to_sql(symbol, engine)

dfAll = pd.DataFrame()

for name in df.code:
    dfAll = dfAll.append(pd.read_sql(\
    f'SELECT Date, "Adj Close" AS "{name}" FROM "{name}" WHERE Date > "2020-01-01"',engine))

dfAll = dfAll.groupby("Date").sum()

dfAll.head()
