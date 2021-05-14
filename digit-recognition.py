from PIL import Image
import imgformatter as imgf
import tensorflow as tf 

img = Image.open('digits/digit.jpg').convert('L')
img = imgf.mnist_formatter(img)
model = tf.keras.models.load_model('digits.model')
print(model.predict(img))
