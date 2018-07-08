import pandas as pd
import numpy as np
df = pd.read_csv('weather.csv')
#first five rows of dataframe
print('*'*50)
print(df.head())
#first 10 rows of dataframe
print('*'*50)
print(df.head(10))
#basic statistics on the particular dataset
print('*'*50)
print("1.sum")
print(df.sum())

print('*'*50)
print("2.Row wise Sum")
print(df.sum(1))

print('*'*50)
print("3.mean")
print(df.mean())

print('*'*50)
print("4.Summarizing or detail of data")
print(df.describe())

print('*'*50)
print("5.include string")
print(df.describe(include=['object']))

print('*'*50)
print("6.include number")
print(df.describe(include=['number']))

print('*'*50)
print("7.includes All")
print(df.describe(include='all'))

#last five rows of data frame
print('*'*50)
print(df.tail())
#Extract 2 column
df1 =df[df.columns[1]]
print(df1.describe(include=['object']))





