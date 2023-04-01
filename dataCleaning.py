import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#https://www.python-graph-gallery.com/stacked-and-percent-stacked-barplot
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', 1000)
############################################# Check how many eths 1 count are for meth....
df = pd.read_csv('coinData2023-03-02.csv', encoding='UTF8')
df.loc[df['URL'].str.strip().str[-1] == '/', 'URL'] = df['URL'].str[:-1]
df = df.drop_duplicates(subset=['URL', 'coin', 'count', 'month']) # add 'Month'
df = df.reset_index() #752
# df = df.loc[df['coin'] == 'monero']['count'].count()
# df = df.loc[df['count'] == 14]
# df = df['count'].value_counts()
# df.loc[df['URL'].str[:-1] == '/', 'URL'] = True
# print(df[['count', 'URL']])
print(df)
########################################
# df2 = pd.read_csv('onionAddressesFeb.csv', encoding='UTF8')
# df3 = pd.read_csv('onionAddressesFeb2.csv', encoding='UTF8')
# frames = [df2, df3]
# df = pd.concat(frames)
# # df = df.loc[~df['URL'].str.contains('link=')] # 784
# df = df.loc[(df['type'] == 'litecoin')]
# # df = df.drop_duplicates(subset=['website', 'type', 'count'])
#
# print(df[['address', 'website']])
###############################################
# df = pd.read_csv('onionAddressesBalance2.csv', encoding='UTF8')
# df = df.drop_duplicates(subset=['address', 'type']) #620
# df = df.reset_index()
# df = df.drop(index=[18,45])
# df = df.loc[df['totalReceived'] == 0]
# print(df[['type', 'address']])
# print(df.count())
##############################################
##############################################

# df = pd.read_csv('onionAddressesBalance2.csv', encoding='UTF8')
# print(len(df.index))
# df = df.drop_duplicates(subset=['address'])
# print(len(df.index))
# df = df.reset_index()
# df = df.drop(index=[18,45]) #dropping non-crypto addresses
#
# dfB = df.loc[df['type'] == 'bitcoin']['type'].count()
# dfM = df.loc[df['type'] == 'monero']['type'].count()
# dfE = df.loc[df['type'] == 'ethereum']['type'].count()
# dfL = df.loc[df['type'] == 'litecoin']['type'].count()
# dfZ = df.loc[df['type'] == 'zcash']['type'].count()
#
# print(dfM, dfB, dfL, dfE, dfZ)
#
# df1 = df.loc[df['subtype'] == 'Bech32']['subtype'].count()
# df2 = df.loc[df['subtype'] == 'P2SH']['subtype'].count()
# df3 = df.loc[df['subtype'] == 'P2PKH']['subtype'].count()
# df4 = df.loc[df['subtype'] == 'main']['subtype'].count()
# df5 = df.loc[df['subtype'] == 'subaddress']['subtype'].count()
#
# print(df1, df2, df3, df4, df5)
#
#
# data = [dfM, dfB, dfL, dfE, dfZ]
# labels = ['XMR', 'BTC', 'LTC', 'ETH', 'ZEC']
# print(data)
# colors = sns.color_palette('pastel')[0:5]
#
# plt.pie(data, labels = labels, colors = colors, autopct='%.0f%%')
# plt.show()
#
# print(df[['subtype', 'address']])

###############################################
###########################


# df = df.drop_duplicates(subset=['address'])


# df = df.drop([4,9]) #4=, 9
# df = df.loc[df['type'] == 'litecoin']
# df = df.reset_index()
#
# print(df[['address', 'website', 'type']])
# print(dfB, dfM, dfE, dfL)
# df = df.loc[(~df['URL'].str.contains('.jpg'))&(~df['URL'].str.contains('.webp'))&(~df['URL'].str.contains('.jpeg'))&(~df['URL'].str.contains('.pdf'))&(~df['URL'].str.contains('.png'))]
############################################################
#
# df2 = pd.read_csv('coinDataFeb2.csv', encoding='UTF8')
# df3 = pd.read_csv('coinDataFeb.csv', encoding='UTF8')
# frames = [df2, df3]
# df = pd.concat(frames)
# df = df.drop_duplicates(subset=['URL', 'count', 'coin'])
# df = df.reset_index()
# # df.loc[df['URL'].str.strip().str[-1] == '/', 'URL'] = df['URL'].str[:-1]
# df = df.loc[~df['URL'].str.contains('link=')] # might not need
# df = df.drop_duplicates(subset=['URL', 'count', 'coin'])
#
# dfMonero = df.loc[df['coin'] == 'monero']['count'].sum() #.count()
# dfBitcoin = df.loc[df['coin'] == 'bitcoin']['count'].sum()
# dfEth = df.loc[df['coin'] == 'ethereum']['count'].sum()
# dfLit = df.loc[df['coin'] == 'litecoin']['count'].sum()
# dfZcash = df.loc[df['coin'] == 'zcash']['count'].sum()
#
# df = df.reset_index()
# print(df[['URL', 'count', 'coin']])
# #
# data = [dfMonero, dfBitcoin, dfLit, dfEth, dfZcash]
# print(sum(data), data)
# labels = ['XMR', 'BTC', 'LTC', 'ETH', 'ZEC']
# colors = sns.color_palette('pastel')[0:5]
#
# plt.pie(data, labels = labels, colors = colors, autopct='%.0f%%')
# plt.show()
#################################################################




# df = df.loc[(df['coin'] == 'litecoin')&(df['count'] >= 5)]
# print(df[['URL', 'count']])
# print(df[['coin', 'count']])
# df = df.loc[(df['coin'] == 'zcash')&(df['count'] >= 100)]
# print(dfMonero, dfBitcoin, dfEth, dfLit, dfZcash)



# df.to_csv('onionAddressesMega45.csv', encoding='UTF8')





# import matplotlib.pyplot as plt
# import squarify    # pip install squarify (algorithm for treemap)
# import pandas as pd
#
# # Create a data frame with fake data
# # df = pd.DataFrame({'nb_people':[dfM, dfB, dfL, dfE], 'group':['XMR', 'BTC', 'LTC', 'ETH'] })
#
# # plot it
# squarify.plot(sizes=df['nb_people'], label=df['group'], alpha=.8 )
# plt.axis('off')
# plt.show()
######################################
# #https://www.python-graph-gallery.com/13-percent-stacked-barplot
# import seaborn as sns
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.patches as mpatches
#
# df1 = pd.read_csv('coinData2023-02-18.csv', encoding='UTF8')
# df1['month'] = 'February'
# df2 = pd.read_csv('coinDataTesting2.csv', encoding='UTF8')
# df2['month'] = 'January'
# df3 = pd.read_csv('coinData2023-03-02.csv', encoding='UTF8')
# frames = [df1, df2, df3]
# df = pd.concat(frames)
# df = df.reset_index()
# df.loc[df['URL'].str.strip().str[-1] == '/', 'URL'] = df['URL'].str[:-1]
# df = df.drop_duplicates(subset=['URL', 'coin', 'count', 'month'])
# df = df.reset_index()
#
# df1 = df[df['coin'] == 'litecoin']['count'].count()
# df2 = df[df['coin'] == 'monero']['count'].count()
# df3 = df[df['coin'] == 'ethereum']['count'].count()
# df4 = df[df['coin'] == 'bitcoin']['count'].count()
# df5 = df[df['coin'] == 'zcash']['count'].count()
#
# print(df1, df2, df3, df4, df5)
#
# # libraries
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib import rc
# import pandas as pd
#
# monero = df[df.coin=='monero'].groupby('month')['count'].count()
# print(monero)
# bitcoin = df[df.coin=='bitcoin'].groupby('month')['count'].count()
# ethereum = df[df.coin=='ethereum'].groupby('month')['count'].count()
# print(ethereum)
# litecoin = df[df.coin=='litecoin'].groupby('month')['count'].count()
# print(litecoin)
# zcash = df[df.coin=='zcash'].groupby('month')['count'].count()
# print(zcash)
#
#
# # Data
# r = [0, 1, 2]
# raw_data = {'monero': monero, 'bitcoin': bitcoin, 'ethereum': ethereum, 'litecoin': litecoin, 'zcash': zcash} #,'blueBars': [2, 15, 18, 5, 10]
# df = pd.DataFrame(raw_data)
# # From raw value to percentage
# totals = [i+j+k+m for i,j,k,m,l in zip(df['monero'], df['bitcoin'], df['ethereum'], df['litecoin'], df['zcash'])] #df['blueBars']
# moneroBars = [i / j * 100 for i, j in zip(df['monero'], totals)]
# bitcoinBars = [i / j * 100 for i, j in zip(df['bitcoin'], totals)]
# ethereumBars = [i / j * 100 for i, j in zip(df['ethereum'], totals)]
# litecoinBars = [i / j * 100 for i, j in zip(df['litecoin'], totals)]
# zcashBars = [i / j * 100 for i, j in zip(df['zcash'], totals)]
#
#
# print(moneroBars, bitcoinBars, ethereumBars, litecoinBars)
# bars = [ethereumBars, bitcoinBars, moneroBars, litecoinBars]
# # plot
# barWidth = 0.55
# names = ('Jan', 'Feb', 'Mar')
# plt.bar(r, moneroBars, color='#b5ffb9', edgecolor='white', width=barWidth, label='XMR')
# plt.bar(r, bitcoinBars, bottom=moneroBars, color='#f9bc86', edgecolor='white', width=barWidth, label='BTC')
# plt.bar(r, ethereumBars, bottom=[i + j for i, j in zip(moneroBars, bitcoinBars)], color='#a3acff', edgecolor='white',
#         width=barWidth, label='ETH')
# plt.bar(r, litecoinBars, bottom=[i + j + k for i, j, k in zip(moneroBars, bitcoinBars, ethereumBars)], color='#f4a3ff', edgecolor='white', width=barWidth, label='LTC')
# plt.bar(r, zcashBars, bottom=[i + j + k + l for i, j, k, l in zip(moneroBars, bitcoinBars, ethereumBars, litecoinBars)], color='#a3fff0', edgecolor='white', width=barWidth, label='ZEC')
#
# plt.xticks(r, names)
# # for bar in bars:
# #     for i, v in enumerate(bar):
# #         plt.text(i, v+1, str(round(v, 1)), ha='center')
#
# for i, v in enumerate(bitcoinBars):
#     plt.text(i, 50, str(round(v, 1)) + '%', ha='center', fontsize=8)
#
# for i, v in enumerate(moneroBars):
#     plt.text(i, v-10, str(round(v, 1)) + '%', ha='center', fontsize=8)
#
# for i, v in enumerate(ethereumBars):
#     plt.text(i, 100-v, str(round(v, 1)) + '%', ha='center', fontsize=8)
#
# for i, v in enumerate(litecoinBars):
#     plt.text(i, 100-v, str(round(v, 1)) + '%', ha='center', fontsize=8)
#
# for i, v in enumerate(zcashBars):
#     plt.text(i, 100-v, str(round(v, 1)) + '%', ha='center', fontsize=8)
# plt.xlabel("2023, 2.5k onion sites")
# plt.legend(loc='upper left', bbox_to_anchor=(1,1), ncol=1)
# # Show graphic
# plt.show()
# plt.savefig('pic.png')

########################################################################
# load dataset
# tips = df
#
# # set the figure size
# plt.figure(figsize=(7, 7))
#
# # from raw value to percentage
# total = tips.groupby('month')['count'].count().reset_index()
# print(total)
# monero = tips[tips.coin=='monero'].groupby('month')['count'].count().reset_index()
# print(monero)
# bitcoin = tips[tips.coin=='bitcoin'].groupby('month')['count'].count().reset_index()
# print(bitcoin)
# litecoin = tips[tips.coin=='litecoin'].groupby('month')['count'].count().reset_index()
# print(litecoin)
# ethereum = tips[tips.coin=='ethereum'].groupby('month')['count'].count().reset_index()
# print(ethereum)
#
# ethereum['count'] = [i / j * 100 for i,j in zip(ethereum['count'], total['count'])]
# print(ethereum['count'])
# # litecoin['count'] = [i / j * 100 for i,j in zip(litecoin['count'], total['count'])]
# bitcoin['count'] = [i / j * 100 for i,j in zip(bitcoin['count'], total['count'])]
# print(bitcoin['count'])
# monero['count'] = [i / j * 100 for i,j in zip(monero['count'], total['count'])]
# print(monero['count'])
# total['count'] = [i / j * 100 for i,j in zip(total['count'], total['count'])]
# print(total['count'])
# bar1 = sns.barplot(x="month",  y="count", data=total, color='darkblue')
# bar2 = sns.barplot(x="month",  y="count", data=bitcoin, color='blue')
# bar3 = sns.barplot(x="month", y="count", data=monero, color='lightblue')
# bar5 = sns.barplot(x="month", y="count", data=ethereum, color='red')
#
# # add legend
# top_bar = mpatches.Patch(color='darkblue', label='Total')
# mid_bar = mpatches.Patch(color='blue', label='Bitcoin')
# bottom_bar = mpatches.Patch(color='lightblue', label='Monero')
# # bottom_bar2 = mpatches.Patch(color='black', label='Litecoin')
# bottom_bar3 = mpatches.Patch(color='red', label='Ethereum')
#
#
# plt.legend(handles=[top_bar, mid_bar, bottom_bar,bottom_bar3])
#
# # show the graph
# plt.show()
# print(df)











