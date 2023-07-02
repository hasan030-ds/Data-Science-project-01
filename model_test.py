#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import pickle 
import numpy as np


# In[2]:


df = pd.read_excel(r"C:\Users\Hasan Shaik\Desktop\datasets\CAR DETAILS FROM CAR DEKHO.xlsx")


# In[5]:


model = pickle.load(open(r"C:\Users\Hasan Shaik\Downloads\fwd2\LinearRegressionModel.pkl",'rb'))


# In[6]:


#testing
model.predict(pd.DataFrame(columns=['name','year','km_driven','fuel','seller_type','transmission','owner'],data=np.array(['Renault KWID RXT',2016,40000,'Petrol','Individual','Manual','Firts Owner']).reshape(1,7)))


# In[7]:


225000 - 268461.17886433


# In[8]:


model.predict(pd.DataFrame(columns=['name','year','km_driven','fuel','seller_type','transmission','owner'],data=np.array(['Hyundai i20 Magna 1.4 CRDi',2014,80000,'Diesel','Individual','Manual','Second Owner']).reshape(1,7)))


# In[9]:


# actual price 409999
# our model 410005.11718693
410005.11718693- 409999


# In[ ]:





# In[ ]:





# In[ ]:




