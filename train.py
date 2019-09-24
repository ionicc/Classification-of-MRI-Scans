import numpy as np 
from tqdm import tqdm
import cv2
import os
import shutil
import itertools
import imutils
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split

from keras.preprocessing.image import ImageDataGenerator
from keras.applications.vgg16 import VGG16, preprocess_input
from keras import layers
from keras.models import Model, Sequential
from keras.optimizers import Adam, RMSprop
from keras.callbacks import EarlyStopping

from keras.models import Model, load_model
from keras.layers import Input
from keras.layers.core import Dropout, Lambda
from keras.layers.convolutional import Conv2D, Conv2DTranspose
from keras.layers.pooling import MaxPooling2D
from keras.layers.merge import concatenate
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras import backend as K
import keras

TRAIN_DIR = r'E:\Github projects\Classification-of-MRI-Scans\resized data\TRAIN'
VAL_DIR = r'E:\Github projects\Classification-of-MRI-Scans\resized data\VAL'
TEST_DIR = r'E:\Github projects\Classification-of-MRI-Scans\resized data\TEST'

train_datagen = ImageDataGenerator(
    rotation_range=15,
    width_shift_range=0.1,
    height_shift_range=0.1,
    shear_range=0.1,
    brightness_range=[0.5, 1.5],
    horizontal_flip=True,
    vertical_flip=True,
    preprocessing_function=preprocess_input
)

test_datagen = ImageDataGenerator(
    preprocessing_function=preprocess_input
)

train_generator = train_datagen.flow_from_directory(
    TRAIN_DIR,
    color_mode='rgb',
    target_size=(224,224),
    batch_size=32,
    class_mode='binary',
    seed=123
)

validation_generator = test_datagen.flow_from_directory(
    VAL_DIR,
    color_mode='rgb',
    target_size=(224,224),
    batch_size=16,
    class_mode='binary',
    seed=123
)

vgg = VGG16(
    weights='imagenet',
    include_top=False, 
    input_shape=(224,224) + (3,)
)

vgg16 = Sequential()
vgg16.add(vgg)
vgg16.add(layers.Dropout(0.2))
vgg16.add(layers.Flatten())
vgg16.add(layers.Dropout(0.5))
vgg16.add(layers.Dense(1, activation='sigmoid'))

vgg16.layers[0].trainable = False



vgg16.compile(
    loss='binary_crossentropy', 
    optimizer=keras.optimizers.Adam(lr=0.0003, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0, amsgrad=False), 
    metrics=["accuracy"])

vgg16.summary()

vgg16_train = vgg16.fit_generator(
    train_generator,
    steps_per_epoch=50,
    epochs=120,
    validation_data=validation_generator,
    validation_steps=30,
)

