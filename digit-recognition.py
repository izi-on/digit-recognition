from PIL import Image
import imgformatter as imgf
import tensorflow as tf 
import numpy as np

img = Image.open('digits/digit.jpg').convert('L')
img = imgf.mnist_formatter(img)

img.show()

img = np.array(img)
n_img = []

for i in range(28):
    for j in range(28):
        n_img.append(img[i,j])

model = tf.keras.models.load_model('digits.model')
print(model.predict(n_img))
