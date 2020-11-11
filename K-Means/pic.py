import numpy as np
import PIL.Image as image
from sklearn import preprocessing
from sklearn.cluster import KMeans


def load_data(filePath):
  f = open(filePath, 'rb')
  img = image.open(f)
  width, height = img.size
  data = []
  for x in range(width):
    for y in range(height):
      c1, c2, c3 = img.getpixel((x, y))
      data.append([c1, c2, c3])
  f.close()

## 为了加快聚类的收敛，进行MM规范化
  mm = preprocessing.MinMaxScaler()
  data = mm.fit_transform(data)
  return np.mat(data), width, height

img, width, height = load_data('./weixin.jpg')

kmeans = KMeans(n_clusters=2)
kmeans.fit(img)
label = kmeans.predict(img)

# convert the predict result to img size matrix
label = label.reshape([width, height])

pic_mark = image.new('L', (width, height))
for x in range(width):
  for y in range(height):
    pic_mark.putpixel((x, y), int(256/(label[x][y]+1))-1)

pic_mark.save("weixin_mark.jpg", "JPEG")