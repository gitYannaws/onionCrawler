import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_colwidth', -1)

# df1 = pd.read_csv('coinData.csv')
df2 = pd.read_csv('coinData2.csv')
df3 = pd.read_csv('coinData3.csv')
df4 = pd.read_csv('coinData3.csv')

frames = [df2, df3, df4]
df = pd.concat(frames)


#2332
dfM = df.loc[((df['coin'] == 'monero')|(df['coin'] == 'xmr'))&(df['count'] != 0)]['count'].count()
dfB = df.loc[((df['coin'] == 'bitcoin')|(df['coin'] == 'btc'))&(df['count'] != 0)]['count'].count()
dfL = df.loc[((df['coin'] == 'litecoin')|(df['coin'] == 'ltc'))&(df['count'] != 0)]['count'].count()
dfE = df.loc[((df['coin'] == 'ethereum')|(df['coin'] == r'\beth'))&(df['count'] != 0)]['count'].count()
dfZ = df.loc[((df['coin'] == 'zcash')|(df['coin'] == 'zec'))&(df['count'] != 0)]['count'].count()

# df = df.loc[(df['coin'] == 'zc23ash')|(df['coin'] == r'\beth\b')]
# df = df.loc[((df['coin'] == 'monero')|(df['coin'] == 'xmr'))&(df['count'] != 0)]['count']
df = df.loc[df['coin'] == 'ltc']
df = df.reset_index()

print(df[['URL', 'count']])


print("")
print(dfM)
print(dfB)
print(dfL)
print(dfE)
print(dfZ)

# df.to_csv("totalCoinData", sep='\t')

# data = [dfM, dfB, dfL, dfE, dfZ]
# labels = ['XMR', 'BTC', 'LTC', 'ETH', 'ZEC']
#
# #define Seaborn color palette to use
# colors = sns.color_palette('pastel')[0:5]
#
# #create pie chart
# plt.pie(data, labels = labels, colors = colors, autopct='%.0f%%')
# plt.show()