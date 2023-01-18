# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VIKo2qMInvQ0VBPLKcnJBeUxOod0u4bm
"""

import pandas as pd
import numpy as np

data=pd.read_excel("/content/Bank_Personal_Loan_Modelling.xlsx")

data

data.info()

data.nunique()

data.isnull().sum()

data.drop(['ID','ZIP Code'],axis=1,inplace=True)

data

data.columns

num_columns=['Age','Experience','Income','Family','CCAvg','Mortgage']

num_columns

cat_columns=['Education','Personal Loan','Securities Account','CD Account','Online','CreditCard']

data[cat_columns]=data[cat_columns].astype('category')

data.info()

x=data.drop(['Personal Loan'],axis=1)
y=data['Personal Loan']

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression( )

lr.fit(x,y)

import pickle

print('saving model as pkl file.......')
pickle.dump(lr,open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))

