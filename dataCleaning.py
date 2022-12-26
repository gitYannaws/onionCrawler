import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_colwidth', -1)

df = pd.read_csv('coinData.csv')
#2332
dfM = df.loc[((df['coin'] == 'monero')|(df['coin'] == 'xmr'))&(df['count'] != 0)]['count'].sum()
dfB = df.loc[((df['coin'] == 'bitcoin')|(df['coin'] == 'btc'))&(df['count'] != 0)]['count'].sum()
dfL = df.loc[((df['coin'] == 'litecoin')|(df['coin'] == 'ltc'))&(df['count'] != 0)]['count'].sum()
dfE = df.loc[((df['coin'] == 'ethereum')|(df['coin'] == r'\beth'))&(df['count'] != 0)]['count'].sum()
dfZ = df.loc[((df['coin'] == 'zcash')|(df['coin'] == 'zec'))&(df['count'] != 0)]['count'].sum()

# df = df.loc[((df['coin'] == 'zcash')|(df['coin'] == 'zec'))&(df['count'] != 0)]

df = df.loc[df['count'] >= 10]

print(df[['coin', 'URL']])
# print(dfM)
# print(dfB)
# print(dfL)
# print(dfE)
# print(dfZ)