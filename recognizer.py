import cv2
import os
import pandas as pd
import numpy as np
from sklearn import tree

def load_images_from_folder(folder):
    images = []
    for filename in np.arange(1, 51, 1):
        filename = folder + "/" + str(filename) + ".png"
        img = cv2.imread(filename)
        if img is not None:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # cv2.imshow('Image',img)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
            img = cv2.resize(img, (28, 28))
            images.append(img)
    return images
def predict(test_image):
    image_nums = 50
    # read image
    url = "Kanji_dataset/"
    img = load_images_from_folder(url + "Image")
    img = np.array(img)
    img = img.reshape(image_nums, 784)
    # read label
    jisho = pd.read_csv(url + "Meaning.csv")
    jisho = jisho.values
    label = np.arange(1, 51, 1)
    img = img
    clf = tree.DecisionTreeClassifier()
    clf.fit(img, label)
    #print(img[0])
    #Testing
    #test_image = cv2.imread("/home/hieunguyen/Documents/Kanji_dataset/Image/6.png")
    test_image = cv2.resize(test_image, (28, 28))
    # cv2.imshow('Image',test_image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    test_image = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)
    test_image = test_image.reshape(1, 784)
    y_predict = clf.predict(test_image)
    #print(y_predict)
    # load dictionary
    #print(jisho[y_predict - 1])
    return jisho[y_predict - 1]