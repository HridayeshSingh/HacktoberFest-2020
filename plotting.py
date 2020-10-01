# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 22:00:06 2020

@author: Hridayesh Singh
"""

import numpy as np
import seaborn as sns
import pandas as pd
data = pd.read_csv('E:/Machine Learning/GClassroom Content/mobile_cleaned-1549119762886.csv')
data.head()
type(data)
ax = sns.scatterplot(x="stand_by_time", y="battery_capacity", data = data)
ax = sns.scatterplot(x = "stand_by_time", y = "battery_capacity", hue = "thickness", data = data)
ax = sns.distplot(data["stand_by_time"])
ax = sns.distplot(data["stand_by_time"], bins = 10)
ax = sns.distplot(data["stand_by_time"], bins = 30)
ax = sns.distplot(data["stand_by_time"], kde = False, rug = True, bins = 40)
ax = sns.boxplot(x = "is_liked", y = "battery_capacity", data = data)

uniform_data = np.random.rand(2,3)
np.ravel(uniform_data)
ax = sns.scatterplot(data = "uniform_data")
