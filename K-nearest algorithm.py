"""
K-NN algorithm is arguably the simplest machine learning algorithm
building the model consists only of storing the training dataset
to make prediction for a new data point, the algorithm finds the nearest closest points in the training dataset
this is the nearest neighbors

k-neighbors classification
only considers exactly one nearest neighbor, which is the closest training data point to the point
we want to make a prediction for. The prediction is then simply the known output for this training point
"""

import mglearn
import matplotlib.pyplot as plt
import sklearn
from sklearn.datasets import load_breast_cancer
import numpy as np

X, y = mglearn.datasets.make_forge()
mglearn.discrete_scatter(X[:,0], X[:,1],y)
mglearn.plots.plot_knn_classification(n_neighbors=3)
plt.legend(['Class 0', 'Class 1'], loc=4)
plt.xlabel('First feature')
plt.ylabel('Second feature ')
print('X.shape:{}'.format(X.shape))
plt.show()
"""
can also consider an arbitrary number, k, of neighbors 
cosidering more than one neighbor, use a voting to assign a label 
for each test point, count how many neighbors belong to class 0 ad how 
many neighbors belong to class 1 
then assign the class that is more frequent 
"""

"""
apply k-nearest neighbors algorithm using scikit-learn 
split our data into a training and a test set so we can evaluate generalization performance 
"""

from sklearn.model_selection import train_test_split
X,y = mglearn.datasets.make_forge()
X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=0)

#import instantiate the class - set parameters like the number of neighbors to use
from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(n_neighbors=3)
#fit the classifier using the training set - storing dataset to compute neighbors during prediction
clf.fit(X_train, y_train)
# make predictions on the test data
# this computes its nearest neighbors in the training set and finds the most common class
print('test set prediction: {}'.format(clf.predict(X_test)))
#to evaluate how well our model generalizes - call the score method with the test data together
print('test set accuracy: {:.2f}'.format(clf.score(X_test, y_test)))

"""
Confirming the connectio between model complexity and generalization that we discussed 
earlier. We will do this on the real-world Breast Cancer dataset. Begin by splitting the dataset 
into a training and a test set. evaluate training and test set performance with different numbers of neighbors
"""

from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
    cancer.data, cancer.target, stratify=cancer.target, random_state=66)

training_accuracy = []
test_accuracy = []
#trying neighbors from 1 to 10
neighbors_settings = range(1,11)

for n_neighbors in neighbors_settings:
    # building the model
    clf = KNeighborsClassifier(n_neighbors=n_neighbors)
    clf.fit(X_train, y_train)
    # record training set accuracy
    training_accuracy.append(clf.score(X_train,y_train))
    #test_accuracy generalization
    test_accuracy.append(clf.score(X_test,y_test))

plt.plot(neighbors_settings, training_accuracy, label='training accuracy')
plt.plot(neighbors_settings, test_accuracy, label='test accuracy')
plt.ylabel('Accuracy')
plt.xlabel('n_neighbors')
plt.legend()
plt.show()

"""
considering lower neighbors corresponds to a more complex model - the plot is horizontally flipped 
the more neighbors that are introduced the less accurate the model gets 
the best performance is somewhere between a single neighbor and using too many that make the model too simple

"""