import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', 1000)
#############################################
# df = pd.read_csv('coinDataTesting1.csv', encoding='UTF8')
# df.loc[df['URL'].str.strip().str[-1] == '/', 'URL'] = df['URL'].str[:-1]
# df = df.drop_duplicates(subset=['URL', 'coin', 'count'])
# df = df.loc[df['count'] == 17]
# df = df['count'].value_counts()
# df.loc[df['URL'].str[:-1] == '/', 'URL'] = True
# print(df[['coin', 'URL']])
# print(df)
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
# df = pd.read_csv('onionAddressesBalance.csv', encoding='UTF8')
# df = df.drop_duplicates(subset=['address', 'type']) #620
# df = df.reset_index()
# df = df.loc[df['type'] == 'litecoin']
# print(df[['address', 'type', 'website']])
##############################################
##############################################
#
# df2 = pd.read_csv('onionAddressesFeb.csv', encoding='UTF8')
# df3 = pd.read_csv('onionAddressesFeb2.csv', encoding='UTF8')
# frames = [df2, df3]
# df = pd.concat(frames)
#
# df = df.drop_duplicates(subset=['address'])
#
#
# dfB = df.loc[df['type'] == 'bitcoin']['type'].count()
# dfM = df.loc[df['type'] == 'monero']['type'].count()
# dfE = df.loc[df['type'] == 'ethereum']['type'].count()
# dfL = df.loc[df['type'] == 'litecoin']['type'].count()
# dfZ = df.loc[df['type'] == 'zcash']['type'].count()
#
# print(dfM, dfB, dfL, dfE, dfZ)

# df1 = df.loc[df['subtype'] == 'Bech32']['subtype'].count()
# df2 = df.loc[df['subtype'] == 'P2SH']['subtype'].count()
# df3 = df.loc[df['subtype'] == 'P2PKH']['subtype'].count()
# df4 = df.loc[df['subtype'] == 'main']['subtype'].count()
# df5 = df.loc[df['subtype'] == 'subaddress']['subtype'].count()
#
# print(df1, df2, df3, df4, df5)
#
# #
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
# dfMonero = df.loc[df['coin'] == 'monero']['count'].sum()
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