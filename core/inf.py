import pandas as pd
import numpy as np

df = pd.read_csv("CPIHOSSL.csv")
print(df.head())
df2 = df.query("DATE == '9/1/2022'")
print(df2)
"""
for i in priceHistory:
    infl = inflationData[inflationData.DATE ==
                             '9/1/'+i['date'][:4]]['CPIHOSSL']
    temp.append(i['price']*curr/infl)
    temp = [price] + temp
    print(temp)
    volatility = np.std(temp)
    print(volatility)
"""
