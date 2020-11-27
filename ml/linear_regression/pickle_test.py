import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import matplotlib.pyplot as plt
import pickle

data = pd.read_csv('student-mat.csv', sep = ';')

data = data[['G1', 'G2', 'G3', 'studytime', 'failures', 'absences']]
predict = 'G3'
x = np.array(data.drop([predict], 1))
y = np.array(data[predict])
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = 0.1)
#loads the previously trained model present in "student_model.pickle"
linear = pickle.load(open('student_model.pickle', 'rb'))

print(linear.coef_, linear.intercept_)

predictions = linear.predict(x_test)

for i in range(len(predictions)):
    print(int(predictions[i]), x_test[i], y_test[i])
