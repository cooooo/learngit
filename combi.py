# -*- coding: utf-8 -*-
"""
Created on Sat Aug 06 17:24:34 2016

@author: Sargas
"""

from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
import numpy as np
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
y = np.array([1, 1, 1, 2, 2, 2])
clf = QuadraticDiscriminantAnalysis()
clf.fit(X, y)
print(clf.predict([[-0.8, -1]]))