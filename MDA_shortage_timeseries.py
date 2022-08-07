
import pandas as pd
import numpy as np
from numpy import array
from numpy import hstack
my_seed = 636
np.random.seed(my_seed)
import random 
random.seed(my_seed)
import tensorflow as tf
tf.random.set_seed(my_seed)
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.preprocessing.sequence import TimeseriesGenerator


data_ts = pd.read_csv("shortage.csv")
data_ts=np.array(data_ts)
data_ts=data_ts[0:39,1:7]
ndarrayts = np.transpose(data_ts)
Datats = ndarrayts
Datats = Datats.astype('float64')
# define generator
n_features = Datats.shape[1]
n_input = 2
generatorts = TimeseriesGenerator(Datats,Datats, length=n_input, batch_size=1)
# number of samples
print('Samples: %d' % len(generatorts))
# define model
modelts = Sequential()
modelts.add(LSTM(100, activation='relu', input_shape=(n_input, n_features)))
modelts.add(Dense(38))
#modelts.compile(optimizer='adam', loss='mse')
optimizer =tf.optimizers.Adam(learning_rate=0.001)
modelts.compile(optimizer=optimizer, loss='mae')
# fit model
modelts.fit(generatorts, steps_per_epoch=1, epochs=500, verbose=0)
# make a one step prediction out of sample
# make a one step prediction out of sample
x_input = array([Datats[4],
Datats[5]]).reshape((1, n_input, n_features))
yhat = modelts.predict(x_input, verbose=0)
np.set_printoptions(suppress=True) 
print(yhat)