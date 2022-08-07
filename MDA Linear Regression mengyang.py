# -*- coding: utf-8 -*-
"""
Created on Tue May 11 16:34:41 2021

@author: User
"""

import numpy as np
import pandas as pd

from sklearn import linear_model
import matplotlib.pyplot as plt

# %matplotlib inline
import seaborn as sns
sns.set()

#read csv file
data = pd.read_csv('D:\KU Leuven\Modern Data Analytics\project\98-17c.csv')
data = data.dropna( )
data.head()

# SDG 6.4.2. Water Stress (%) is the target
y = data.values[:,-10]

#create the design / feature matrix
X1 = data.drop(labels=None,axis=1, index=None, columns='SDG 6.4.2. Water Stress (%)', inplace=False)
X2 = X1.values[:,:]
X = np.delete(X2,obj=0, axis=1)
futures_names = X1.columns[1:]


#setting up the ridge model
Alpha1 = 0.1
ridge_model = linear_model.Ridge(fit_intercept=True, alpha=Alpha1,copy_X=True,normalize=True)
ridge_model.fit(X,y)
print('Coefficients for Ridge Model, alphs:',str(Alpha1))
print(ridge_model.coef_[:])



# Setting up the Lasso Model without normalize
# Here can find the important features
Alpha2 = 10
lasso_model2 = linear_model.Lasso(alpha=Alpha2, normalize=False, max_iter=2000)
lasso_model2.fit(X,y)
print('Coefficients for Lasso Model, alpha:',str(Alpha2))
print(lasso_model2.coef_[:])

Alpha2 = 50
lasso_model3 = linear_model.Lasso(alpha=Alpha2,normalize=False,  max_iter=2000)
lasso_model3.fit(X,y)
print('Coefficients for Lasso Model, alpha:',str(Alpha2))
print(lasso_model3.coef_[:])


# Return the coefficient of determination R^2 of the prediction.
print('RSquared Ridge')
print(ridge_model2.score(X,y))
print('RSquared Lasso')
print(lasso_model3.score(X,y))


# Plot the coefficient for different values of Alpha in Lasso Model
alpha = np.power(10,np.arange(0,2,0.1))

weights = np.zeros((len(alpha),len(futures_names)),dtype=float)
for i in np.arange(0,len(alpha)):
    Lasso_model = linear_model.Lasso(fit_intercept=True, 
                                     alpha=alpha[i],
                                     copy_X=True,
                                     normalize=False, max_iter=2000)
    Lasso_model.fit(X,y)
    weights[i,:]= Lasso_model.coef_

plt.figure(figsize=(10,7))    
for i in np.arange(0,len(futures_names)):
    plt.semilogx(alpha[:],weights[:,i]*100,label=futures_names[i])

plt.xlabel('log(alpha)')
plt.ylabel('weight')
plt.legend(bbox_to_anchor=(1.05, 1),loc="upper left");
