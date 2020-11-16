from PIL import Image 

pic1 = Image.open('lena_modified.png')
pic2 = Image.open('lena.png')

weight, height = pic1.size

for i in range(0, weight):
  for j in range(0, height):
    if pic2.getpixel((i,j)) == pic1.getpixel((i,j)):
      pic1.putpixel((i,j),(255,255,255,0))

pic1.save('pic_diff.png')

