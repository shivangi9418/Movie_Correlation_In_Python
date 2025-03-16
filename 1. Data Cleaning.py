import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('movies.csv')
# print(df.head())

#Look for missing data, if any
for col in df.columns:
    pct_missing=np.mean(df[col].isnull())
    print(f'{col} - {pct_missing}%')


#Changing data type of columns/Type Conversion
df['budget']=pd.to_numeric(df['budget'].astype(int))
df['gross']=pd.to_numeric(df['gross'].astype(int))

#Adding new column 'correct_year'
df['correct_year']=df['released'].astype(str).str.split().str[2]

# #Sorting the data wrt gross revenue
df=df.sort_values(by=['gross'],inplace=False,ascending=False)

# #To see all of the data
pd.set_option('display.max_rows',None)

#Drop any duplicates
df['company'].drop_duplicates().sort_values(ascending=False)

df.to_csv('movies.csv',index=False)
print(df)
print(df.info())