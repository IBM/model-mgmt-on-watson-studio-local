
# coding: utf-8

### Setting Dynamic Variables

import sys
ver = sys.argv[1]

# ### Preparing the Dataset

# #### Importing the libraries

# In[88]:


import numpy as np
import pandas as pd


# #### Importing the dataset

# In[89]:

import os
dataset = pd.read_csv(os.environ['DSX_PROJECT_DIR']+'/datasets/Wine.csv')
X = dataset.iloc[:, 0:13].values  #Explanatory variables
y = dataset.iloc[:, 13].values  #Target variable


# In[90]:


dataset.head(2)


# In[91]:


X[0:2]


# In[82]:


y[0:2]


# ### Feature Engineering

# #### Feature Scaling

# In[92]:


from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X = sc.fit_transform(X)


# In[93]:


X[0:2]


# #### Applying PCA

# In[94]:


from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
X = pca.fit_transform(X)


# In[95]:


X[0:2]


# In[96]:


explained_variance = pca.explained_variance_ratio_
explained_variance*100


# ### Exporting the results

# In[97]:


features = pd.DataFrame(X)
features.to_csv(os.environ['DSX_PROJECT_DIR']+'/datasets/features'+'-'+ver+'.csv')
features.head(2)


# In[98]:


target = pd.DataFrame(y)
target.to_csv(os.environ['DSX_PROJECT_DIR']+'/datasets/target'+'-'+ver+'.csv')
target[0:2]

