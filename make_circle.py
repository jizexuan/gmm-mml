#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 21:43:48 2017

@author: abriosi
"""

from sklearn.datasets import make_circles
import matplotlib.pyplot as plt
from mdl_gmm import MdlGmm

X,y=make_circles(n_samples=1000, shuffle=True, noise=0.05, random_state=1338, factor=0.6)

plt.title('Circle Data')
plt.scatter(X[:,0],X[:,1],alpha=0.2,s=10)
plt.show()

unsupervised=MdlGmm(plots=True)
unsupervised.fit(X)
samples=unsupervised.sample(500)

plt.title('Sampled from GMM')
plt.scatter(samples[:,0],samples[:,1],alpha=0.2,s=10)
plt.show()

