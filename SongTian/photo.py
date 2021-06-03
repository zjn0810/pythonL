from PIL import Image

import numpy as np

'''
a = np.array(Image.open("photo.jpg"))

print(a.shape,a.dtype)

b = [255, 255, 255] -a

im = Image.fromarray(b.astype('uint8'))

im.save('photo1.jpg')
'''
'''
a = np.array(Image.open("photo.jpg").convert('L'))

print(a.shape,a.dtype)

b =255 - a

im = Image.fromarray(b.astype('uint8'))

im.save('photo1.jpg')
'''

a = np.array(Image.open("photo.jpg").convert('L'))

print(a.shape,a.dtype)

b =(100/255) * a + 150  

im = Image.fromarray(b.astype('uint8'))

im.save('photo1.jpg')


















