from figures.Rectangle import Rectangle
import numpy as np
import matplotlib.pyplot as plt
from figures.Circle import Circle
from figures.Triangle import Triangle
from figures.Generator import Generator
from model.Dataset import Dataset
from model.Model import Model
import tensorflow as tf
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

gen = Generator()
img = gen.generate_db(8000, 0.2)

ds = Dataset()
X_train, y_train = ds.load(mode="train")
X_test, y_test = ds.load(mode="test")

X_test = X_test / 255
X_train = X_train / 255

my_model = Model()

input_layer = tf.keras.layers.Input((128, 128, 1))
output = my_model(input_layer)
final_model = tf.keras.Model(input_layer, output)

final_model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
    loss=tf.keras.losses.mean_absolute_error,
    metrics=[tf.keras.losses.mean_absolute_error]
)
final_model.fit(
    X_train,
    y_train,
    validation_data=(X_test, y_test),
    epochs=5,
)
final_model.save("test_model", save_format="tf")