from PIL import Image
import math

def mnist_formatter(img):

    img_n = Image.new('L', (28,28), color = 'black')

    width, height = img.size
    step_h = height/28
    step_w = step_h
    start_h = height/2-14*step_h
    start_w = width/2-14*step_w

    pixel_n = img_n.load()
    pixel_o = img.load()

    print(pixel_n[0,0])

    for i in range(img_n.size[0]):
        for j in range(img_n.size[1]):
            
            bp = 0
            for b in range(math.floor(step_w)):
                for h in range(math.floor(step_h)):
                    bp += pixel_o[math.floor(i*step_w+start_w+b), math.floor(j*step_h+start_h+h)]
            bp = int(bp/(math.floor(step_w)*math.floor(step_h)))
            
            #bp = pixel_o[math.floor(i*step_w+start_w), math.floor(j*step_h+start_h)]
            pixel_n[i,j] = bp
                
    return img_n
            