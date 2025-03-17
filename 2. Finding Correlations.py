import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm
import statsmodels.api as sa 

df=pd.read_csv('movies.csv')

#Budget high correlation -> Movies with higher budgets tend to generate higher gross revenue.
#Company high correlation -> Movies produced by major studios (like 20th Century Fox, Disney, etc.) might have a higher chance of generating significant revenue.

#Scatter plot with budget vs gross
plt.scatter(x=df['budget'],y=df['gross'])
plt.title('Budget vs Gross Earnings')
plt.xlabel('Budget for Film')
plt.ylabel('Gross Earnings')
# plt.grid()
# plt.show()

#Plot budget vs gross using seaborn
sns.regplot(x='budget',y='gross',data=df,scatter_kws={'color':'red'},line_kws={'color':'purple'})
# plt.show()

#Let's start looking at correlation

bdf=df.select_dtypes(include=[int,float]).corr(method='pearson').copy()
print(bdf)
#There is infact a high correlation between budget and gross.


correlation_matrix=bdf.corr(method='pearson')
sns.heatmap(correlation_matrix,annot=True)
plt.title('Correlation Matric for Numeric Features')
plt.xlabel('Movie Features')
plt.ylabel('Movie Features')
plt.show()

#Negative values in correlations: For instance, in your case, a negative correlation between budget and gross might indicate that movies with higher budgets tend to have lower gross revenue, and vice versa.
# This could be due to a number of factors, such as high-budget movies being more experimental or niche, and therefore appealing to a smaller audience.

#Unstacking and forming pairs
correlation_mat=bdf.corr()
corr_pairs=correlation_mat.unstack()
# print(corr_pairs)
sorted_pairs=corr_pairs.sort_values()
# print(sorted_pairs)

#Looking for high correlation pairs
high_corr=sorted_pairs[(sorted_pairs)>0.5]
print(high_corr)

#Votes and Budget have the highest correlation to gross earnings


