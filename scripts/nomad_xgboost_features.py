
# coding: utf-8

### Setting Dynamic Variables

import sys
ver = sys.argv[1]

# In[14]:


import os
import pandas as pd
import numpy as np

train=pd.read_csv(os.environ['DSX_PROJECT_DIR']+'/datasets/train.csv')
test=pd.read_csv(os.environ['DSX_PROJECT_DIR']+'/datasets/test.csv.gz')


# In[15]:


train[0:3]


# In[16]:


test[0:3]


# In[7]:


def generate_features(train_df):
#     train_df['atoms_al']=round(train_df.percent_atom_al*train_df.number_of_total_atoms*2)/2
#     train_df['atoms_ga']=round(train_df.percent_atom_ga*train_df.number_of_total_atoms*2)/2
#     train_df['atoms_in']=round(train_df.percent_atom_in*train_df.number_of_total_atoms*2)/2

#     train_df['al_ga_sum']=train_df['atoms_al']+train_df['atoms_ga']
#     train_df['al_in_sum']=train_df['atoms_al']+train_df['atoms_in']
#     train_df['ga_in_sum']=train_df['atoms_ga']+train_df['atoms_in']

#     train_df['al_minus_ga']=train_df['atoms_al']-train_df['atoms_ga']
#     train_df['al_minus_in']=train_df['atoms_al']-train_df['atoms_in']
#     train_df['ga_minus_in']=train_df['atoms_ga']-train_df['atoms_in']

#     train_df['al_ga_minus_in']=train_df['atoms_al']+train_df['atoms_ga']-train_df['atoms_in']
#     train_df['al_in_minus_ga']=train_df['atoms_al']+train_df['atoms_in']-train_df['atoms_ga']
#     train_df['ga_in_minus_al']=train_df['atoms_ga']+train_df['atoms_in']-train_df['atoms_al']

#     train_df['al_ga_ratio']=train_df['percent_atom_al']/train_df['percent_atom_ga']
#     train_df['al_in_ratio']=train_df['percent_atom_al']/train_df['percent_atom_in']
#     train_df['ga_in_ratio']=train_df['percent_atom_ga']/train_df['percent_atom_in']

#     train_df['al_all_ratio']=train_df['percent_atom_al']/(train_df['percent_atom_ga']+train_df['percent_atom_in'])
#     train_df['ga_all_ratio']=train_df['percent_atom_ga']/(train_df['percent_atom_al']+train_df['percent_atom_in'])
#     train_df['in_all_ratio']=train_df['percent_atom_in']/(train_df['percent_atom_al']+train_df['percent_atom_ga'])


#     train_df['al_ga_sum_ratio']=train_df['al_ga_sum']/train_df['number_of_total_atoms']
#     train_df['al_in_sum_ratio']=train_df['al_in_sum']/train_df['number_of_total_atoms']
#     train_df['ga_in_sum_ratio']=train_df['ga_in_sum']/train_df['number_of_total_atoms']


    train_df['lattice_angle_alpha_degree_minus90']=train_df['lattice_angle_alpha_degree'] - 90.0
    train_df['lattice_angle_beta_degree_minus90']=train_df['lattice_angle_beta_degree'] - 90.0
    train_df['lattice_angle_gamma_degree_minus90']=train_df['lattice_angle_gamma_degree'] - 90.0
    
    return(train_df)


# In[8]:


# train=generate_features(train)
# test=generate_features(test)

bandgap_energy_ev_mean=(np.log(train.groupby('spacegroup')['bandgap_energy_ev'].mean())).to_dict()
formation_energy_ev_natom_mean=(np.log(train.groupby('spacegroup')['formation_energy_ev_natom'].mean())).to_dict()

train['bandgap_energy_ev_mean']=train['spacegroup'].map(bandgap_energy_ev_mean)
train['formation_energy_ev_natom_mean']=train['spacegroup'].map(bandgap_energy_ev_mean)

test['bandgap_energy_ev_mean']=test['spacegroup'].map(bandgap_energy_ev_mean)
test['formation_energy_ev_natom_mean']=test['spacegroup'].map(bandgap_energy_ev_mean)


# In[12]:


train.to_csv(os.environ['DSX_PROJECT_DIR']+'/datasets/train_features'+'-'+ver+'.csv')
train[0:3]


# In[13]:


test.to_csv(os.environ['DSX_PROJECT_DIR']+'/datasets/test_features'+'-'+ver+'.csv')
test[0:3]

