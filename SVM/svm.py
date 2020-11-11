import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('./data.csv')
pd.set_option('display.max_columns', None)
# print(data.columns)
# print(data.head(5))
# print(data.describe())

features_mean = list(data.columns[2:12])
features_se = list(data.columns[12:22])
features_worst = list(data.columns[22:32])

data.drop("id", axis=1, inplace=True)
data['diagnosis'] = data['diagnosis'].map({'M':1, 'B':0})

# sns.countplot(data['diagnosis'], label='Count')
# plt.show()

# corr = data[features_mean].corr()
# plt.figure(figsize=(14,14))
# sns.heatmap(corr, annot=True)
# plt.show()

features_remain = ['radius_mean', 'texture_mean', 'smoothness_mean', 'compactness_mean', 'symmetry_mean', 'fractal_dimension_mean']

# features_remain = data.columns[1:31]

train, test = train_test_split(data, test_size=0.3)
train_X = train[features_remain]
train_y = train['diagnosis']
test_X = test[features_remain]
test_y = test['diagnosis']

ss = StandardScaler()
train_X = ss.fit_transform(train_X)
test_X = ss.transform(test_X)

model = svm.SVC()
# model = svm.LinearSVC()
model.fit(train_X, train_y)
prediction = model.predict(test_X)
print('Accuracy is ', metrics.accuracy_score(prediction, test_y))
