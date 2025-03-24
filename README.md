# 🎬**Introduction**

This is a data analysis project focused on finding correlations between variables in the movie industry dataset. It harnesses python and its libraries like Pandas,Seaborn, and Matplotlib.

# 📌**Project Overview**

The project involves the following key steps:

* **Data Acquisition:** Downloading a movie industry dataset from Kaggle. The dataset contains data like budget, company, genre, gross revenue, movie name, and release date.
  
* **Environment Setup:** Installation of a Python environment with Jupyter Notebooks (available through Anaconda).
  
* **Data Analysis:** Examining the dataset to determine correlations between several factors and gross revenue of movies.
  
* **Data Cleaning and Formatting:** Formatting and cleaning the data, including dealing with missing data and fixing data types.
  
* **GitHub Upload:** Posting the finished project on a GitHub repository.

# 💻**Code and its output**

**1. 🧹Data Cleaning**

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

**2. ⚖️Finding Correlations**


#Scatter plot with budget vs gross

      plt.scatter(x=df['budget'],y=df['gross'])
      
      plt.title('Budget vs Gross Earnings')
      
      plt.xlabel('Budget for Film')
      
      plt.ylabel('Gross Earnings')
      
      plt.grid()
      
      plt.show()

output:

![plot between budget and gross earnings](https://github.com/user-attachments/assets/1792a573-625b-4dfd-8d2e-d18a7287d8ac)

#Plot budget vs gross using seaborn

    sns.regplot(x='budget',y='gross',data=df,scatter_kws={'color':'red'},line_kws={'color':'purple'})
    
    plt.show()

output:

![plot between budget and gross earnings using seaborn](https://github.com/user-attachments/assets/27a16524-0546-44de-8e4b-53f1ce1b4e1f)

#Let's start looking at correlation

      bdf=df.select_dtypes(include=[int,float]).corr(method='pearson').copy()
      
      print(bdf)

output:

|          | year      | score     | votes     | budget    | gross     | runtime   |
|----------|-----------|-----------|-----------|-----------|-----------|-----------|
| year     | 1.000000  | 0.097435  | 0.222851  | 0.309861  | 0.262374  | 0.120145  |
| score    | 0.097435  | 1.000000  | 0.409157  | 0.054659  | 0.185943  | 0.398956  |
| votes    | 0.222851  | 0.409157  | 1.000000  | 0.486606  | 0.632717  | 0.308996  |
| budget   | 0.309861  | 0.054659  | 0.486606  | 1.000000  | 0.750031  | 0.269185  |
| gross    | 0.262374  | 0.185943  | 0.632717  | 0.750031  | 1.000000  | 0.244996  |
| runtime  | 0.120145  | 0.398956  | 0.308996  | 0.269185  | 0.244996  | 1.000000  |

#Let's look at the correlation

      correlation_matrix=bdf.corr(method='pearson')
      
      sns.heatmap(correlation_matrix,annot=True)
      
      plt.title('Correlation Matric for Numeric Features')
      
      plt.xlabel('Movie Features')
      
      plt.ylabel('Movie Features')
      
      plt.show()

output:

![Figure_1_corrected](https://github.com/user-attachments/assets/61f03a89-431e-4e8a-a3eb-0c29da8ac0c5)

#Unstacking and forming pairs

      correlation_mat=bdf.corr()
      
      corr_pairs=correlation_mat.unstack()
      
      print(corr_pairs)

output:

| Column 1 | Column 2 | Correlation |
|----------|----------|-------------|
| year     | year     | 1.000000    |
|          | score    | -0.548066   |
|          | votes    | -0.399805   |
|          | budget   | -0.000381   |
|          | gross    | -0.154856   |
|          | runtime  | -0.553560   |
| score    | year     | -0.548066   |
|          | score    | 1.000000    |
|          | votes    | 0.026573    |
|          | budget   | -0.733194   |
|          | gross    | -0.529023   |
|          | runtime  | 0.291717    |
| votes    | year     | -0.399805   |
|          | score    | 0.026573    |
|          | votes    | 1.000000    |
|          | budget   | 0.328489    |
|          | gross    | 0.587975    |
|          | runtime  | -0.231366   |
| budget   | year     | -0.000381   |
|          | score    | -0.733194   |
|          | votes    | 0.328489    |
|          | budget   | 1.000000    |
|          | gross    | 0.861841    |
|          | runtime  | -0.350270   |
| gross    | year     | -0.154856   |
|          | score    | -0.529023   |
|          | votes    | 0.587975    |
|          | budget   | 0.861841    |
|          | gross    | 1.000000    |
|          | runtime  | -0.401560   |
| runtime  | year     | -0.553560   |
|          | score    | 0.291717    |
|          | votes    | -0.231366   |
|          | budget   | -0.350270   |
|          | gross    | -0.401560   |
|          | runtime  | 1.000000    |

      sorted_pairs=corr_pairs.sort_values()
      
      print(sorted_pairs)

output:
| Column 1 | Column 2 | Correlation |
|----------|----------|-------------|
| score    | budget   | -0.733194   |
| budget   | score    | -0.733194   |
| runtime  | year     | -0.553560   |
| year     | runtime  | -0.553560   |
| score    | year     | -0.548066   |
| year     | score    | -0.548066   |
| score    | gross    | -0.529023   |
| gross    | score    | -0.529023   |
|          | runtime  | -0.401560   |
| runtime  | gross    | -0.401560   |
| year     | votes    | -0.399805   |
| votes    | year     | -0.399805   |
| runtime  | budget   | -0.350270   |
| budget   | runtime  | -0.350270   |
| votes    | runtime  | -0.231366   |
| runtime  | votes    | -0.231366   |
| year     | gross    | -0.154856   |
| gross    | year     | -0.154856   |
| budget   | year     | -0.000381   |
| year     | budget   | -0.000381   |
| votes    | score    | 0.026573    |
| score    | votes    | 0.026573    |
|          | runtime  | 0.291717    |
| runtime  | score    | 0.291717    |
| votes    | budget   | 0.328489    |
| budget   | votes    | 0.328489    |
| gross    | votes    | 0.587975    |
| votes    | gross    | 0.587975    |
| budget   | gross    | 0.861841    |
| gross    | budget   | 0.861841    |
| votes    | votes    | 1.000000    |
| year     | year     | 1.000000    |
| gross    | gross    | 1.000000    |
| budget   | budget   | 1.000000    |
| score    | score    | 1.000000    |
| runtime  | runtime  | 1.000000    |

#Looking for high correlation pairs
      high_corr=sorted_pairs[(sorted_pairs)>0.5]
      
      print(high_corr)

output:
| Column 1 | Column 2 | Correlation |
|----------|----------|-------------|
| gross    | votes    | 0.587975    |
| votes    | gross    | 0.587975    |
| budget   | gross    | 0.861841    |
| gross    | budget   | 0.861841    |
| votes    | votes    | 1.000000    |
| year     | year     | 1.000000    |
| gross    | gross    | 1.000000    |
| budget   | budget   | 1.000000    |
| score    | score    | 1.000000    |
| runtime  | runtime  | 1.000000    |

#Votes and Budget have the highest correlation to gross earnings
