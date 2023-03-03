#!/usr/bin/env python
# coding: utf-8

# In[1]:


#packages for data analysis
import numpy as np
import pandas as pd

from sklearn import svm

#visualize data
import matplotlib.pyplot as plt
import seaborn as sns; sns.set(font_scale=1.2)

get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


recipes = pd.read_csv('MvC.csv')
print(recipes.head())


# In[3]:


#plot our data
sns.lmplot('Flour','Sugar',data=recipes,hue='Type',
          palette='Set1',fit_reg=False,scatter_kws={"s":70});


# In[4]:


#format or pre-process our data
type_label = np.where(recipes['Type']=='Muffin',0,1)
recipe_features = recipes.columns.values[1:].tolist()
recipe_features
ingredients = recipes[['Flour','Sugar']].values
print(ingredients)


# In[5]:


#fit model

model = svm.SVC(kernel='linear')
model.fit(ingredients, type_label)


# In[6]:


#get the separating hyperplane
w = model.coef_[0]
a = -w[0] / w[1]
xx = np.linspace(30,60)
yy = a * xx - (model.intercept_[0] / w[1])


#plot the aprallels to the separating hyperplanes that pass through the support vectors
b = model.support_vectors_[0]
yy_down = a * xx + (b[1] - a * b[0])
b = model.support_vectors_[-1]
yy_up = a * xx + (b[1] - a * b[0])


# In[7]:


sns.lmplot('Flour','Sugar',data=recipes,hue='Type',palette='Set1',fit_reg=False,scatter_kws={"s":70});
plt.plot(xx,yy,linewidth=2, color = 'black')
plt.plot(xx,yy_down,'k--')
plt.plot(xx,yy_up,'k--')


# In[8]:


#create function to predict muffin or cupcake
def muff_or_cupc(flour,sugar):
    if(model.predict([[flour,sugar]]))==0:
        print("You're looking at a muffin recipe!")
    else:
        print("You're looking at a cupcake recipe!")

muff_or_cupc(50,20)


# In[10]:


##### Plot it on graph
sns.lmplot('Flour','Sugar',data=recipes,hue='Type',palette='Set1',fit_reg=False,scatter_kws={"s":70});
plt.plot(xx,yy,linewidth=2, color = 'black')
plt.plot(50,20,'yo',markersize='9')
