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
      ## 为了看到对应的原图，将每个类别的点的rgb值设置为该簇质心点的rgb，即簇内的点的特征均为质心点的特征。把0-255投射到1-256
      data.append([(c1+1)/256.0, (c2+1)/256.0, (c3+1)/256.0])
  f.close()
  return np.mat(data), width, height

img, width, height = load_data('./weixin.jpg')

kmeans = KMeans(n_clusters=16)
label = kmeans.fit_predict(img)
label = label.reshape([width, height])
# print(label)

img = image.new('RGB', (width, height))
for x in range(width):
  for y in range(height):
    c1 = kmeans.cluster_centers_[label[x, y], 0]
    c2 = kmeans.cluster_centers_[label[x, y], 1]
    c3 = kmeans.cluster_centers_[label[x, y], 2]
    img.putpixel((x,y), (int(c1*256)-1,int(c2*256)-1,int(c3*256)-1))
img.save('weixin_new.jpg')


