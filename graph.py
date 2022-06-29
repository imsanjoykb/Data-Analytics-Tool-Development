import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('https://raw.githubusercontent.com/marsja/jupyter/master/flanks.csv',
                 index_col=0)

fig = plt.figure(figsize=(12, 8))

df = pd.read_csv('https://vincentarelbundock.github.io/Rdatasets/csv/datasets/mtcars.csv')

ax = sns.regplot(x="wt", y="mpg", data=df)
plt.show()
