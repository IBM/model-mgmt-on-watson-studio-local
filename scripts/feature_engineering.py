# coding: utf-8

import os
import sys

# #### Importing the libraries
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Setting Dynamic Variables
ver = sys.argv[1]

# #### Importing the dataset

dataset = pd.read_csv(os.environ['DSX_PROJECT_DIR']+'/datasets/Wine.csv')
X = dataset.iloc[:, 0:13].values  # Explanatory variables
y = dataset.iloc[:, 13].values  # Target variable
dataset.head(2)
X[0:2]
y[0:2]

# ### Feature Engineering
# #### Feature Scaling
sc = StandardScaler()
X = sc.fit_transform(X)
X[0:2]

# #### Applying PCA
pca = PCA(n_components=2)
X = pca.fit_transform(X)
X[0:2]

explained_variance = pca.explained_variance_ratio_
explained_variance*100

# ### Exporting the results
features = pd.DataFrame(X)
features.to_csv(os.environ['DSX_PROJECT_DIR'] +
                '/datasets/features' + '-' + ver + '.csv')
features.head(2)

target = pd.DataFrame(y)
target.to_csv(os.environ['DSX_PROJECT_DIR'] +
              '/datasets/target' + '-' + ver + '.csv')
target[0:2]
