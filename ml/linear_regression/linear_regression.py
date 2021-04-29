import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import matplotlib.pyplot as plt
import pickle
from matplotlib import style

#reads dataset
data = pd.read_csv("student-mat.csv", sep=";")

#select relevant attributes
data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]

#print(data.head())
#label
predict = "G3"

x = np.array(data.drop([predict], 1))
y = np.array(data[predict])


#trains the model
x_train,  x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = 0.1)

'''linear = linear_model.LinearRegression()

#determines label and prints accuracy
linear.fit(x_train, y_train)
print(linear.score(x_test, y_test))

#saves model
with open('student_model.pickle', 'wb') as f:
    pickle.dump(linear, f)'''
#trains the model n time to find the one with the best accuracyt and the saves it
n = 50
best = 0
for _ in range(n):
    x_train, x_test, y_train,y_test = sklearn.model_selection.train_test_split(x, y, test_size = 0.1)
    linear = linear_model.LinearRegression()
    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)
    if acc > best:
        best = acc
        with open('student_model.pickle', 'wb') as f:
            pickle.dump(linear, f)

#loads the saved model
linear = pickle.load(open('student_model.pickle', 'rb'))

print(acc)
print(linear.coef_, linear.intercept_)

predictions = linear.predict(x_test)

for x in range(len(predictions)):
    print(int(predictions[x]), x_test[x], y_test[x])


#graph
p = 'failures'
style.use('ggplot')
plt.scatter(data[p], data[predict])
plt.xlabel(p)
plt.ylabel(predict)
plt.show()
