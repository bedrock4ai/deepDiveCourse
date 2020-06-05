# -*- coding: utf-8 -*-
"""1 Session - AI Deep Dive

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rNeLv3oL4a6M8A4gS64adyperJPKpIho
"""

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

#url = 'https://github.com/bedrock4ai/deepDiveCourse/blob/master/1%20Session%20-%20AI%20Deep%20Dive%20-%20Data%20Analysis.xlsx'

url = 'https://raw.githubusercontent.com/bedrock4ai/deepDiveCourse/master/1%20Session%20-%20AI%20Deep%20Dive%20-%20Data%20Analysis.csv'

df1 = pd.read_csv(url)
# Dataset is now stored in a Pandas Dataframe

print (df1)

df1.columns

mean1 = df1['Sales'].mean()
min1 = df1['Sales'].min()
max1 = df1['Sales'].max()
print('Mean: ', mean1)
print('Min: ', min1)
print('Max: ', max1)

import seaborn as sns
sns.scatterplot(x='Temperature', 
           y='Sales',
          data = df1)