from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd
import numpy as np

data = pd.read_csv('data.csv', encoding='gbk')
train_x = data[['2019年国际排名', '2018世界杯', '2015亚洲杯']]
df = pd.DataFrame(train_x)
kmeans = KMeans(n_clusters=3)

mm = preprocessing.MinMaxScaler()
train_x = mm.fit_transform(train_x)
kmeans.fit(train_x)
predict_y = kmeans.predict(train_x)

result = pd.concat((data, pd.DataFrame(predict_y)),axis=1)
result.rename({0:u'聚类'}, axis=1, inplace=True)
print(result)