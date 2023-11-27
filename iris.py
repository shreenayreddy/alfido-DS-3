# -*- coding: utf-8 -*-
"""iris

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hW9fLzXjDCRCbnlQ5df0tUYWu2yvdVf1
"""

# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/186UKWtBdhzbo7QOejjfJjgKasuhg-MVz
"""

import pandas as pd
import numpy as np
import sklearn.cluster as KMeans
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("/content/Iris.csv")
df.head()

df["Species"],categories=pd.factorize(df["Species"])
df.head()

df.describe()

df.isna().sum()

from mpl_toolkits.mplot3d import Axes3D
fig=plt.figure()
ax=fig.add_subplot(111,projection="3d")
ax.scatter(df.PetalLengthCm,df.PetalWidthCm,df.Species)
ax.set_xlabel("PetalLengthCm")
ax.set_ylabel("PetalWidthCm")
ax.set_zlabel("Species")
plt.title("3D Scatter Plot Example")
plt.show()

colors = ['red', 'orange', 'pink']
species = ['Iris-virginica','Iris-versicolor','Iris-setosa']

sns.scatterplot(data=df,x="PetalLengthCm",y="PetalWidthCm",hue="Species")

sns.scatterplot(data=df,x="SepalLengthCm",y="SepalWidthCm",hue="Species")

df['Species'].hist()

df["SepalWidthCm"].hist()

df["PetalWidthCm"].hist()

df["PetalLengthCm"].hist()

df = df.drop(columns = ['Id'])
df.head()

corr = df.corr()
fig, ax = plt.subplots(figsize=(5,4))
sns.heatmap(corr, annot=True, ax=ax, cmap = 'Spectral')

from sklearn.model_selection import train_test_split
X = df.drop(columns=['Species'])
Y = df['Species']
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.30)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(x_train, y_train)
print("Accuracy: ",model.score(x_test, y_test) * 100)

from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier()
model.fit(x_train, y_train)
print("Accuracy: ",model.score(x_test, y_test) * 100)

from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
model.fit(x_train, y_train)
print("Accuracy: ",model.score(x_test, y_test) * 100)