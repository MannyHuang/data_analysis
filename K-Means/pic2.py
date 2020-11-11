import numpy as np
import PIL.Image as image
from sklearn import preprocessing
from sklearn.cluster import KMeans
from skimage import color

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

  mm = preprocessing.StandardScaler()
  data = mm.fit_transform(data)
  return np.mat(data), width, height

img,width,height = load_data('./weixin.jpg')
kmeans = KMeans(n_clusters=16)
kmeans.fit(img)
label = kmeans.predict(img)
label = label.reshape([width, height])

## unit8类型代表无符号整数，0-255之间，此时输出的图像是颠倒的，可能因为拍摄的时候本身是倒置的
label_color = (color.label2rgb(label)*255).astype(np.uint8)

## 设置三维矩阵转置，让1、2维互换
label_color = label_color.transpose(1, 0, 2)

## fromarray函数可以通过矩阵生成图片
images = image.fromarray(label_color)
images.save('weixin_mark_color.jpg')