**Introduction**

This is a data analysis project focused on finding correlations between variables in the movie industry dataset. It harnesses python and its libraries like Pandas,Seaborn, and Matplotlib.

**Project Overview**

The project involves the following key steps:

* **Data Acquisition:** Downloading a movie industry dataset from Kaggle. The dataset contains data like budget, company, genre, gross revenue, movie name, and release date.
  
* **Environment Setup:** Installation of a Python environment with Jupyter Notebooks (available through Anaconda).
  
* **Data Analysis:** Examining the dataset to determine correlations between several factors and gross revenue of movies.
  
* **Data Cleaning and Formatting:** Formatting and cleaning the data, including dealing with missing data and fixing data types.
  
* **GitHub Upload:** Posting the finished project on a GitHub repository.

**Code and its output**

**1.Data Cleaning**
import pandas as pd

import seaborn as sns

import numpy as np

import matplotlib.pyplot as plt


df=pd.read_csv('movies.csv')

print(df.head())

**output:**
| Name                                     | Rating | Genre  | Year | ....... | Released                             | Score | Country        | Budget      | Gross        | Company                | Runtime | Correct Year |
| :--------------------------------------- | :-----: | :-----: | :---: | :------: | :----------------------------------- | :----: | :-------------: | :----------: | :-----------: | :---------------------- | :------: | :-----------: |
| Avatar                                   | PG-13  | Action | 2009 | ....... | December 18, 2009 (United States) | 7.8  | United States | 237000000 | 2847246203 | Twentieth Century Fox | 162.0   | 2009         |
| Avengers: Endgame                        | PG-13  | Action | 2019 | ....... | April 26, 2019 (United States)    | 8.4  | United States | 356000000 | 2797501328 | Marvel Studios          | 181.0   | 2019         |
| Titanic                                  | PG-13  | Drama  | 1997 | ....... | December 19, 1997 (United States) | 7.8  | United States | 200000000 | 2201647264 | Twentieth Century Fox | 194.0   | 1997         |
| Star Wars: Episode VII - The Force Awakens | PG-13  | Action | 2015 | ....... | December 18, 2015 (United States) | 7.8  | United States | 245000000 | 2069521700 | Lucasfilm              | 138.0   | 2015         |
| Avengers: Infinity War                   | PG-13  | Action | 2018 | ....... | April 27, 2018 (United States)    | 8.4  | United States | 321000000 | 2048359754 | Marvel Studios          | 149.0   | 2018         |

#Look for missing data, if any

for col in df.columns:

    pct_missing=np.mean(df[col].isnull())
    
    print(f'{col} - {pct_missing}%')
  

| Column       | Missing Percentage |
|--------------|--------------------|
| name         | 0.0%               |
| rating       | 0.00941053457064436% |
| genre        | 0.0%               |
| year         | 0.0%               |
| released     | 0.0%               |
| score        | 0.00013070186903672723% |
| votes        | 0.00013070186903672723% |
| director     | 0.0%               |
| writer       | 0.0003921056071101817% |
| star         | 0.00013070186903672723% |
| country      | 0.00013070186903672723% |
| budget       | 0.0%               |
| gross        | 0.0%               |
| company      | 0.0%               |
| runtime      | 0.00026140373807345446% |
| correct_year | 0.0005228074761469089% |

#Changing data type of columns/Type Conversion

df['budget']=pd.to_numeric(df['budget'].astype(int))

df['gross']=pd.to_numeric(df['gross'].astype(int))

print(df.info())

output:

| Column         | Non-Null Count | Dtype   |
|----------------|----------------|---------|
| name           | 7651 non-null  | object  |
| rating         | 7579 non-null  | object  |
| genre          | 7651 non-null  | object  |
| year           | 7651 non-null  | int64   |
| released       | 7651 non-null  | object  |
| score          | 7650 non-null  | float64 |
| votes          | 7650 non-null  | float64 |
| director       | 7651 non-null  | object  |
| writer         | 7648 non-null  | object  |
| star           | 7650 non-null  | object  |
| country        | 7650 non-null  | object  |
| budget         | 7651 non-null  | int64   |
| gross          | 7651 non-null  | int64   |
| company        | 7651 non-null  | object  |

#Adding new column 'correct_year'

df['correct_year']=df['released'].astype(str).str.split().str[2]


#Sorting the data wrt gross revenue

df=df.sort_values(by=['gross'],inplace=False,ascending=False)

print(df.head())

output:
|      name                                | rating | genre  | year | released                             | score | country        |   budget    |     gross     | company                | runtime | correct_year |
| :---------------------------------------: | :----: | :----: | :--: | :-----------------------------------: | :---: | :-------------: | :---------: | :-----------: | :----------------------: | :-----: | :-----------: |
|                Avatar                    | PG-13  | Action | 2009 | December 18, 2009 (United States)   |  7.8  | United States |  237000000  |  2847246203  | Twentieth Century Fox   |  162.0  |     2009     |
|             Avengers: Endgame             | PG-13  | Action | 2019 | April 26, 2019 (United States)      |  8.4  | United States |  356000000  |  2797501328  |     Marvel Studios      |  181.0  |     2019     |
|                 Titanic                   | PG-13  | Drama  | 1997 | December 19, 1997 (United States)   |  7.8  | United States |  200000000  |  2201647264  | Twentieth Century Fox   |  194.0  |     1997     |
| Star Wars: Episode VII - The Force Awakens | PG-13  | Action | 2015 | December 18, 2015 (United States)   |  7.8  | United States |  245000000  |  2069521700  |          Lucasfilm       |  138.0  |     2015     |
|             Avengers: Infinity War            | PG-13  | Action | 2018 | April 27, 2018 (United States)      |  8.4  | United States |  321000000  |  2048359754  |     Marvel Studios      |  149.0  |     2018     |

#Drop any duplicates

df['company'].drop_duplicates().sort_values(ascending=False)


df.to_csv('movies.csv',index=False)

print(df)

print(df.info())

output:
|      name                                | rating | genre    | year | ... |     gross     | company                                      | runtime | correct_year |
| :---------------------------------------: | :----: | :-------: | :--: | :-: | :-----------: | :------------------------------------------- | :-----: | :-----------: |
|                Avatar                    | PG-13  | Action   | 2009 | ... |  2847246203  | Twentieth Century Fox                      |  162.0  |     2009     |
|             Avengers: Endgame             | PG-13  | Action   | 2019 | ... |  2797501328  | Marvel Studios                               |  181.0  |     2019     |
|                 Titanic                   | PG-13  | Drama    | 1997 | ... |  2201647264  | Twentieth Century Fox                      |  194.0  |     1997     |
| Star Wars: Episode VII - The Force Awakens | PG-13  | Action   | 2015 | ... |  2069521700  | Lucasfilm                                    |  138.0  |     2015     |
|             Avengers: Infinity War            | PG-13  | Action   | 2018 | ... |  2048359754  | Marvel Studios                               |  149.0  |     2018     |
|                   ...                     |  ...   |  ...     | ...  | ... |      ...      | ...                                          |  ...    |     ...      |
|           Lion of the Desert            |   PG   | Biography | 1980 | ... |       0       | Falcon International Productions             |  173.0  |     1981     |
|                  Mr. Love                 | PG-13  | Comedy   | 1985 | ... |       0       | Enigma Productions                           |   91.0  |     1986     |
|                 Jack's Back                |   R    | Crime    | 1988 | ... |       0       | Cinema Group                                 |   97.0  |     1988     |
|                  Walker                   |   R    | Biography | 1987 | ... |       0       | In-Cine Compañía Industrial Cinematográfica |   94.0  |     1987     |
|              Jamón, Jamón               |   R    | Comedy   | 1992 | ... |       0       | Lolafilms                                    |   95.0  |     1994     |

| #   | Column         | Non-Null Count | Dtype   |
| :---: | -------------- | -------------- | ------- |
| 0   | name           | 7651 non-null  | object  |
| 1   | rating         | 7579 non-null  | object  |
| 2   | genre          | 7651 non-null  | object  |
| 3   | year           | 7651 non-null  | int64   |
| 4   | released       | 7651 non-null  | object  |
| 5   | score          | 7650 non-null  | float64 |
| 6   | votes          | 7650 non-null  | float64 |
| 7   | director       | 7651 non-null  | object  |
| 8   | writer         | 7648 non-null  | object  |
| 9   | star           | 7650 non-null  | object  |
| 10  | country        | 7650 non-null  | object  |
| 11  | budget         | 7651 non-null  | int64   |
| 12  | gross          | 7651 non-null  | int64   |
| 13  | company        | 7651 non-null  | object  |
| 14  | runtime        | 7649 non-null  | float64 |
| 15  | correct_year   | 7647 non-null  | object  |

**2. Finding Correlations**


#Scatter plot with budget vs gross

plt.scatter(x=df['budget'],y=df['gross'])

plt.title('Budget vs Gross Earnings')

plt.xlabel('Budget for Film')

plt.ylabel('Gross Earnings')

plt.grid()

plt.show()

output:

![plot between budget and gross earnings](https://github.com/user-attachments/assets/1792a573-625b-4dfd-8d2e-d18a7287d8ac)

