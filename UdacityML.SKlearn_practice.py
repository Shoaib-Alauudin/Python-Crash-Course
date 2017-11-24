import numpy as np
X = np.array([[-1,-1],[-2,-1],[-3,-2],[1,1],[2,1],[3,2]])
Y = np.array([1,1,1,2,2,2])
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(X,Y)
GaussianNB()
print(clf .predict([[8,-4]]))

from sklearn.metrics import accuracy_score
print(accuracy_score(clf.predict([[8,-4]]),X))

# from sklearn.naive_bayes import GaussianNB
# clf = GaussianNB()
# clf.fit(features_train, labels_train)
# pred = clf.predict(features_test)
#print("Hello World")