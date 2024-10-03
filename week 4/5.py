import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("BTC_data.csv")
plt.figure()
plt.plot(data['time'], data['close'])
plt.show()
