import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("./magnus_carlsen_games.csv")

resultByFormat = pd.crosstab(dataset['format'], dataset['result'], normalize="index")

print(resultByFormat)

resultByFormat.plot(kind="bar", stacked=True)
plt.show()

# plt.bar(playerName['format'], playerName['id'])
# plt.show()