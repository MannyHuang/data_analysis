import pandas as pd
import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score

train_data = pd.read_csv('./data_analysis/Titanic_Data/train.csv')
test_data = pd.read_csv('./data_analysis/Titanic_Data/test.csv')

# print(train_data.info())
# print('-'*30)
# print(train_data.describe())
# print('-'*30)
# print(train_data.describe(include=['O']))
# print('-'*30)
# print(train_data.head())
# print('-'*30)
# print(train_data.tail())
# print(train_data.isnull().sum())

train_data['Age'].fillna(train_data['Age'].mean(),inplace=True)
test_data['Age'].fillna(test_data['Age'].mean(),inplace=True)
# print(train_data['Embarked'].value_counts())

train_data['Embarked'].fillna('S', inplace=True)
test_data['Embarked'].fillna('S', inplace=True)
train_data['Fare'].fillna(train_data['Fare'].mean(),inplace=True)
test_data['Fare'].fillna(test_data['Fare'].mean(),inplace=True)

features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
train_features = train_data[features]
test_features = test_data[features]
train_labels = train_data['Survived']

dvec = DictVectorizer(sparse=False)
train_features = dvec.fit_transform(train_features.to_dict(orient='record'))
# print(dvec.feature_names_)

clf = DecisionTreeClassifier(criterion='entropy')
clf.fit(train_features, train_labels)

test_features = dvec.transform(test_features.to_dict(orient='record'))
pred_labels = clf.predict(test_features)

acc_decision_tree = round(clf.score(train_features, train_labels), 6)
print(u'Accuracy of score is %.4lf' % acc_decision_tree)
print(u'Accuracy of cross validation score is %.4lf' % np.mean(cross_val_score(clf,train_features, train_labels, cv=10)))