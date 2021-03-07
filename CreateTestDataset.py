# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 15:06:14 2021

@author: Caragea
"""

#%%
# Creating Test DataSets using sklearn.datasets.make_circles 
from sklearn.datasets.samples_generator import make_circles 
from matplotlib import pyplot as plt  
from matplotlib import style 
  
style.use("fivethirtyeight") 
  
X, y = make_circles(n_samples = 200, noise = 0.1) 
plt.scatter(X[:, 0], X[:, 1], s = 40, color ='g') 
plt.xlabel("X") 
plt.ylabel("Y") 
  
plt.show() 
plt.clf()             
        