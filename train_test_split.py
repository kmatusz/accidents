#!/usr/bin/env python
# coding: utf-8

# In[1]:
# Code for train_test_split

import pandas as pd
import numpy as np
import seaborn as sns

import statsmodels.api as sm

from sklearn.model_selection import train_test_split, cross_val_score, cross_validate, KFold
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import FunctionTransformer, OneHotEncoder
from sklearn.impute import SimpleImputer

from sklearn.metrics import roc_auc_score, roc_curve

from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression


pd.set_option("display.max_columns",200)

def print_value_counts(df):
    for i in df.columns:
        print(f'column: {i}')
        display(df[i].value_counts())
        print()


# In[2]:


master_table = pd.read_pickle('data/master_table.pkl')


# In[3]:


master_table.head()


# For each accident in the data, there can be multiple users engaged. This means that we should control for data leakage. People from one accident should be placed together in either train or test dataset. One way to achieve this and simultanously keep distribution of y is to sample accident_id, and from that obtain train test split.

# In[4]:


to_split = master_table[['y', 'accident_id']]


# In[5]:


to_split.groupby('y').count()


# Test what proportion of y we need in both train and test datasets

# In[6]:


to_split.y.value_counts(normalize = True)


# Around 23% of y is equal to 1 (seriously injured or killed).

# Randomly select 30% of accident_id and check the distribution of y obtained:

# In[7]:


temp = pd.DataFrame({'test_id': to_split.accident_id.sample(frac = 0.3), 'if_test': 1}).set_index('test_id')


# In[8]:


temp2 = to_split.set_index('accident_id').join(temp)


# In[9]:


temp2.if_test.isna().mean()


# Through this procedure we have obtained roughly 30% of all people in the dataset for train set.

# In[10]:


temp2.query('if_test == 1').y.mean()


# And percentage of y=1 at 21.7% is close enough to the proportion in the full dataset (23.6%).

# AAAAAA

# In[ ]:





# In[13]:


master_table.groupby('y').accident_id.count()


# Test what proportion of y we need in both train and test datasets

# In[14]:


master_table.y.value_counts(normalize = True)


# Around 23% of y is equal to 1 (seriously injured or killed).

# Randomly select 30% of accident_id and check the distribution of y obtained:

# In[15]:


temp = pd.DataFrame({'test_id': master_table.accident_id.sample(frac = 0.3), 'if_test': 1}).set_index('test_id')


# In[16]:


temp2 = master_table.set_index('accident_id').join(temp)

# In[19]:


temp3 = temp2.reset_index().rename({'index': 'accident_id'}, axis = 1)

temp3.head()

test = temp3.query('if_test == 1').drop('if_test', axis =1)
train = temp3.query('if_test.isna()').drop('if_test', axis =1)

# Check if procedure was correct
print(test.shape)
print(train.shape)

print(test.y.mean())
print(train.y.mean())


train.head()

x_train = train.drop('y', axis = 1)
x_test = test.drop('y', axis = 1)

y_train = train[['y']]
y_test = test[['y']]

