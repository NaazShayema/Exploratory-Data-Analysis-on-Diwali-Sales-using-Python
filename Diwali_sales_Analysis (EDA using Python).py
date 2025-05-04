#!/usr/bin/env python
# coding: utf-8

# In[45]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[2]:


df=pd.read_csv('Diwali Sales Data.csv', encoding='unicode_escape')


# In[3]:


df.shape


# In[4]:


df.head()


# In[5]:


df.info()


# In[6]:


#drop unrelated/blank columns
df.drop(['Status','unnamed1'], axis=1, inplace=True)


# In[7]:


df.info()


# In[8]:


pd.isnull(df)


# In[9]:


#check for null values
pd.isnull(df).sum()


# In[10]:


df.shape


# In[11]:


# drop null values
df.dropna(inplace=True)


# In[12]:


df.shape


# In[13]:


# let's cross-check that null values are removed or not
pd.isnull(df).sum()


# # What is inplace???

# In[14]:


## inplace=True modifies the original DataFrame directly instead of returning a new one.


# In[15]:


### Example


# In[16]:


# initialize list of list
data_test=[['madhav',11],['Gopi',15],['Keshav',],['Lalita',16]]

#Create the pandas DataFrame using list
df_test=pd.DataFrame(data_test, columns=['Name','Age'])
df_test


# In[17]:


df_test.dropna()   # without inplace , the null values are removed 


# In[18]:


df_test     # without inplace , the null values are removed(temporarily) i.e., the null values are still present in original df


# In[19]:


# with inplace
df_test.dropna(inplace=True) 


# In[20]:


df_test


# # both are same
# 
# df_test.dropna(inplace=True)
# 
# df_test=df_test.dropna()

# In[21]:


# change data type
df['Amount']=df['Amount'].astype('int')


# In[22]:


df['Amount'].dtypes


# In[23]:


df.columns


# In[24]:


# rename column
df.rename(columns={'Marital_Status':'Shaadi'})


# In[25]:


# describe() method returns description of the data in the DataFrame(i.e., count, mean, std, etc)
df.describe()


# In[26]:


# use describe() for specific columns
df[['Age','Orders','Amount']].describe()


# # Exploratory Data Analysis

# # Gender

# In[27]:


df.columns


# In[28]:


sns.countplot(x = 'Gender',data = df)


# In[29]:


# plotting a bar chart for Gender and it's count

ax = sns.countplot(x = 'Gender',data = df)

for bars in ax.containers:
    ax.bar_label(bars)


# In[30]:


df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)


# In[32]:


sales_gen=df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)

sns.barplot(x='Gender',y='Amount',data=sales_gen)


# From above graphs we can see that most of the buyers are females and even the purchasing power of females are greater than men

# # Age

# In[33]:


ax = sns.countplot(data = df, x = 'Age Group', hue = 'Gender')

for bars in ax.containers:
    ax.bar_label(bars)


# In[34]:


# Total Amount vs Age Group
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Age Group',y= 'Amount' ,data = sales_age)


# From above graphs we can see that most of the buyers are of age group between 26-35 yrs female

# # State

# In[35]:


# total number of orders from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Orders')


# In[36]:


# total amount/sales from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Amount')


# From above graphs we can see that most of the orders & total sales/amount are from Uttar Pradesh, Maharashtra and Karnataka respectively

# # Marital Status

# In[37]:


ax = sns.countplot(data = df, x = 'Marital_Status')

sns.set(rc={'figure.figsize':(7,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[38]:


sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data = sales_state, x = 'Marital_Status',y= 'Amount', hue='Gender')


# From above graphs we can see that most of the buyers are married (women) and they have high purchasing power

# # Occupation 

# In[39]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Occupation')

for bars in ax.containers:
    ax.bar_label(bars)


# In[40]:


sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Occupation',y= 'Amount')


# From above graphs we can see that most of the buyers are working in IT, Healthcare and Aviation sector

# # Product Category

# In[41]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)


# In[42]:


sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_Category',y= 'Amount')


# From above graphs we can see that most of the sold products are from Food, Clothing and Electronics category

# In[43]:


sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_ID',y= 'Orders')


# In[46]:


# top 10 most sold products (same thing as above)

fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')


# # Conclusion:

# Married women age group 26-35 yrs from UP,  Maharastra and Karnataka working in IT, Healthcare and Aviation are more likely to buy products from Food, Clothing and Electronics category

# In[ ]:




