import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy



a = requests.get('https://api.cryptonator.com/api/full/btc-usd').json()
b = a['ticker']['markets']
df = pd.DataFrame(b)

volume = df['volume']
price = df['price'].astype(float)
market = df['market']
# print(x)
# print(y)

#plt.figure(figsize=[10,10])


for i, txt in enumerate(market):
    plt.annotate(txt, (volume[i], price[i]))


plt.scatter(price,volume)
plt.xlabel('High Price')
plt.ylabel('Volume')
plt.title('Arbitage Graph')
plt.show()

minPrice = min(df['price'])
maxPrice = max(df['price'])
minMarket = min(df['market'])
maxMarket = max(df['market'])
profit = float(maxPrice) - float(minPrice)
percentage = ((float(maxPrice) / float(minPrice)) * 100) - 100


print("" + minMarket + " has lowest BTC price " + minPrice + "")
print("" + maxMarket + "  has higest  BTC  price " + maxPrice + "")
print("If you purchased from " + minMarket + " & sell in to " + maxMarket + " you will get " + str(profit) + " profit which has " + str(percentage) + " %.")









