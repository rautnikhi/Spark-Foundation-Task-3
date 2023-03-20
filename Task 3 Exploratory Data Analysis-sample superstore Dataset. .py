#!/usr/bin/env python
# coding: utf-8

# # GRIP- The Sparks Foundation.
# # Data Science and Business Analytics Internship.
# # Task 3:Explaratory Data analysis- Sample Superstore Dataset.
# # Author : Raut Nikhil Santosh

# # ## Importing Necessary Libraries

# In[1]:


# Analysis
import pandas as pd
import numpy as np

# Visualization 
import matplotlib.pyplot as plt
import seaborn as sns


# # ## Data Loading

# In[2]:


df=pd.read_csv("C:\\Users\\Rohit Bhosale\\Desktop\\SampleSuperstore.csv")


# In[3]:


df.head()


# # ## Data pre-processing

# In[4]:


df.shape


# In[5]:


df.info()


# In[6]:


df.isnull().sum()


# In[7]:


df.describe()


# In[8]:


df.dtypes


# # ## Cheaking the duplication in data

# In[9]:


df.duplicated().sum()


# In[10]:


df.drop_duplicates(inplace=True)


# In[11]:



df.head()


# In[12]:


df.nunique()


# In[13]:


df.columns


# # ## Deleting the Variable

# In[14]:


col=['Postal Code']
df=df.drop(columns=col,axis=1)


# 
# 
# ### Continuous Variables
# #### These are numerical columns like Postal Code,Sales,Quantity,Discount,Profit etc
# 
# ### Categorical Variables
# #### These are columns categories like Ship Mode,Segment, Country,State etc.

# In[15]:


cont_cols=['Sales','Quantity','Discount','Profit'] # For Continuous Columns
cat_cols=['Ship Mode','Segment','Country','City','State','Region','Category','Sub-Category']# Categorical Columns
len(set(cont_cols))+len(set(cat_cols))


# In[16]:


df.select_dtypes(include='number')


# In[17]:


df.select_dtypes(exclude='number')


# # ## 1.Univariate Analysis
# ### *Analyzing one variable
# ### *The displot represents the univariate distribution of data distribution of a variable against the density distribution

# In[18]:


for i in cont_cols:
    plt.figure(figsize=(10,5))
    plt.style.use("tableau-colorblind10")
    sns.distplot(df[i], bins=30, color="r")
    plt.xlabel(i)
    plt.title("Frequency Distribution of"+i)
    plt.xticks(rotation=45)
    plt.show()


# # ## Countplot
# ### It is used to see the Count wise distribution of a categorical entities

# In[19]:


for i in cat_cols:
    plt.figure(figsize=(8,5))
    sns.countplot(df[i])
    plt.xlabel(i)
    plt.title("Count Distribution of"+i)
    plt.xticks(rotation=0)
    plt.grid(True)
    plt.show()


# # ## Boxplot
# ### > It is used to see quartile wise distribution for any continuous variable
# ### > It is also used to see the whether outliers are present in the data or not
# ### > It is used to see quartile wise distribution for any continuous variable against a categorical variable
# ### left line of box : 25th Percentile(Q1)
# ### Right line of box : 75th Percentile(Q3)
# ### Middle line of box : 50th Percentile(Q2)
# ### Inner Quartile Range : IQR : Q3-Q1
# ### Upper (Emperical Relationship): Q3+1.5(Q3-Q1) : Q3+1.5(IQR)
# ### Lower (Emperical Relationship): Q1-1.5(Q3-Q1) : Q1-1.5(IQR)

# In[20]:


for i in cont_cols:
    plt.figure(figsize=(10,5))
    sns.boxplot(df[i])
    plt.xlabel(i)
    plt.title("Statistical Distribution of"+i)
    plt.xticks(rotation=0)
    plt.show()


# # ## Bivariate Analysis
# ### Analyzing two variables
# # ## Scatterplot
# ### It is used to see the relationship between two Continuous variables¶

# In[21]:


for x in cont_cols:
    for y in cont_cols:
        plt.figure(figsize=(10,5))
        if x!=y:
           sns.scatterplot(df[x],df[y],color="r")
           plt.xlabel(x)
           plt.title("Relationship of "+x+" Vs +y")
           plt.xticks(rotation=0)
           plt.grid(True)
           plt.show()


# # ## Line Graph

# In[22]:


plt.figure(figsize=(10,4))
sns.lineplot('Discount','Profit',data=df,color='r',label='Discount')
plt.title('Discount Vs Profit')
plt.legend()
plt.show()


# ### From the above lineplot it is seen that the discount decreases then profit also fall down.

# # ## Pair Plot
# ### A pairplot a pairwise relationships in a dataset.The pairplot function creates a grid of Axes such that each variable in data will by shared in the y-axis across a single row and in the x-axis across a single column.

# In[23]:


g=sns.pairplot(df[cont_cols], height=2.5,diag_kind='kde')
g.fig.suptitle("pair Plot for Continuous variables")


# ### From above pairplot it is seen that more sale does not get more profit it depends on the discount. and when sale is high with low discount it gives us more profit.

# # ## Multivariate Analysis
# ### Analysing multiple variables
# # ## Heat Map
# ### A heatmap is a matrix representation of the variables which is colored based on the intensity of the value.
# ### It provide us with an easy tool to understand the correlation between two entities.

# In[24]:


#Correlation Between Variables.
df[cont_cols].corr()


# In[25]:


plt.figure(figsize=(10,6))
sns.heatmap(df[cont_cols].corr(),annot=True,cmap='Greens')


# ### It is seen that there is weak correlation between the variables.i.e.There is no strong relationship between variables.

# In[26]:


fig=plt.figure()
ax=fig.add_axes([0,0,1,1])

ax.pie(df['Category'].value_counts(),
       labels=["Office Supplies","Furniture","Technology"],
       autopct='%1.2f%%',
       frame=True,
       textprops=dict(color="black",size=12))

ax.axis('equal')
plt.title('Category',
          loc='left',
          color='black',
          fontsize='10')
plt.show()


# In[27]:


df["Ship Mode"].value_counts()


# In[28]:


sns.countplot(x=df["Ship Mode"])


# In[29]:


df["Segment"].value_counts()


# In[30]:


sns.countplot(x=df["Segment"])


# In[31]:


sns.countplot(x=df["Category"])


# ### .From above we can say that the office supply category has highest ratio.

# # ## To check the Statewise profit

# In[32]:


profit=df.groupby(["State"])["Profit"].sum().nlargest(20)
profit


# In[33]:


plt.figure(figsize=(10,5))
profit.plot.bar()


# In[34]:


df1=df.groupby("Region")[["Sales","Profit"]].sum().sort_values(by="Sales",ascending=False)
df1[:].plot.bar(color=["Red","Green"],figsize=(6,5))
plt.title("profit & loss in Region")
plt.show()


# ### . In the West region it get highest profit.
# ### . There are three cities are important in profit California, Newyork and Washington.
# ### . In the central and south region profit is minimum.¶
# ### > We conclude that the California and Newyork have more work and we need to give attention on the central and South region because they give us highest sale with genetating loss. and office supply category have highest supply.

# # Thank you!

# In[ ]:




