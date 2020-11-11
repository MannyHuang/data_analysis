from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_digits
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

digits = load_digits()
data = digits.data
# print(data.shape)
# print(digits.images[0])
# print(digits.target[0])
# plt.gray()
# plt.imshow(digits.images[0])
# plt.show()

train_x, test_x, train_y, test_y = train_test_split(data, digits.target, test_size=0.25, random_state=33)
ss = preprocessing.StandardScaler()
train_ss_x = ss.fit_transform(train_x)
test_ss_x = ss.transform(test_x)

knn = KNeighborsClassifier()
knn.fit(train_ss_x, train_y)
predict_y = knn.predict(test_ss_x)
print('Accuracy of KNN is %.4lf' % accuracy_score(test_y, predict_y))

svm = SVC()
svm.fit(train_ss_x, train_y)
predict_y = svm.predict(test_ss_x)
print('Accuracy of SVM is %.4lf' % accuracy_score(test_y, predict_y))

mm = preprocessing.MinMaxScaler()
train_mm_x = mm.fit_transform(train_x)
test_mm_x = mm.transform(test_x)
mnb = MultinomialNB()
mnb.fit(train_mm_x, train_y)
predict_y = mnb.predict(test_mm_x)
print('Accuracy of MNB is %.4lf' % accuracy_score(test_y, predict_y))

dtc = DecisionTreeClassifier()
dtc.fit(train_mm_x, train_y)
predict_y = dtc.predict(test_mm_x)
print('Accuracy of DTC is %.4lf' % accuracy_score(test_y, predict_y))