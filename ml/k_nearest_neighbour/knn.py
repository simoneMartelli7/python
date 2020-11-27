import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing

#acquires data
data = pd.read_csv('car.data')
#print(data.head())

#changes string values in dataset to integers value
le = preprocessing.LabelEncoder()
buying =  le.fit_transform(list(data['buying']))
maint = le.fit_transform(list(data['maint']))
safety = le.fit_transform(list(data['safety']))
clas = le.fit_transform(list(data['class']))
lug_boot = le.fit_transform(list(data['lug_boot']))
door = le.fit_transform(list(data['door']))
persons = le.fit_transform(list(data['persons']))

predict = 'class'

x = list(zip(buying, maint, door, persons, lug_boot, safety))
y = list(clas)

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = 0.1)
