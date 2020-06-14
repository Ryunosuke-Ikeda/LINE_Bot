#from phlatib import Path
from pathlib import Path
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model
from io import BytesIO


#####  mike=0,siro=1  ######

'''
def predict(img):

    #model_path = "/Users/ryunosuke/Desktop/python/salieri/model_file.hdf5"
    model_path = "./model_file.hdf5"
    classes = ["mike","siro"]
    # load model
    model = load_model(model_path)

    image_size=100

    X = []
    
    image = Image.open(img)
    image = image.convert("RGB")
    image = image.resize((image_size, image_size))
    data = np.asarray(image)
    X.append(data)
    X = np.array(X)
    #正規化(0-1)
    X = X.astype('float32')
    X = X / 255.0

    result = model.predict([X])[0]
    predicted = result.argmax()
    percentage = int(result[predicted] * 100)
    
    return "{0}({1} %)".format(classes[predicted],percentage)
'''
def predict(image):

    #pil_img = Image.open(image)#PILで読み込む
    #img=BytesIO()#空のインスタンスを作る
    #pil_img.save(img,'jpeg')#さっきのインスタンスに保存

    model_path = "./model_file.hdf5"
    classes = ["mike","siro"]
    # load model
    model = load_model(model_path)

    image_size=100

    X = []
    
    image=Image.open(image)
    #image = Image.open(pil_img)
    image = image.convert("RGB")
    image = image.resize((image_size, image_size))
    data = np.asarray(image)
    X.append(data)
    X = np.array(X)
    #正規化(0-1)
    X = X.astype('float32')
    X = X / 255.0

    result = model.predict([X])[0]
    predicted = result.argmax()
    percentage = int(result[predicted] * 100)
    
    return "{0}({1} %)".format(classes[predicted],percentage)
    

#print(predict('/Users/ryunosuke/Desktop/python/original_aug/sample_images/2.jpg'))

