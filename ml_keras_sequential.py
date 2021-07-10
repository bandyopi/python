import numpy as np
import pandas as pd
import tensorflow
from tensorflow import keras

# This module is to predit the the function y=x^2-1
x = np.array([-2, -1,  0, 1, 2, 3, 4, 5, 6, 7, 8], dtype=int)
y = np.array([3, 0, -1, 0, 3, 8, 15, 24, 35, 48, 63], dtype=int)

model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')

model.fit(x, y, epochs=10)

print(model.predict([9]))
