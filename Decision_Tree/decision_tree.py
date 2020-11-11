from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()
features = iris.data
labels = iris.target
train_features, test_features, train_labels, test_labels = train_test_split(features,labels,test_size=0.33,random_state=0)

clf = DecisionTreeClassifier(criterion='gini')
clf = clf.fit(train_features, train_labels)

test_predict = clf.predict(test_features)
score = accuracy_score(test_labels, test_predict)
print("Accuracy rate of %.4lf" % score)
print(iris)

