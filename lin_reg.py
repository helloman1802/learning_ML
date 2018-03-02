import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from sklearn.utils import shuffle
from sklearn.preprocessing import scale
import pandas as pd

X, Y = load_boston(True)

print(load_boston(True))

X, Y = shuffle(X, Y)

X_train = scale(X[:300])

X_test = scale(X[300:])

Y_train = Y[:300]

Y_test = Y[300:]

W = tf.Variable(tf.random_normal([13,1], mean=0.0, stddev=1.0, dtype=tf.float64))
b = tf.Variable(tf.zeros(1, dtype=tf.float64))

x = tf.placeholder(tf.float64)
y = tf.placeholder(tf.float64)

pred = tf.add(b, tf.matmul(x, W))

squared_delta = tf.square(y - pred)

loss = tf.reduce_mean(squared_delta)

init = tf.global_variables_initializer()

optimizer = tf.train.GradientDescentOptimizer(0.01).minimize(loss)

cost_history = []

epochs = 1000

with tf.Session() as sess:
    sess.run(init)

    for i in range(epochs):
        sess.run(optimizer, {x: X_train, y: Y_train})

        if i % 10 == 0:
            cost_history.append(sess.run(loss, {x : X_train, y: Y_train}))

        if i % 100 == 0:
            print(sess.run(loss, {x: X_train, y: Y_train}))

    #plt.plot(cost_history)
    #plt.show()

    print('error on test data', sess.run(loss, { x: X_test, y: Y_test}))
    print('Prediction:{}'.format(sess.run(pred, {x: X_test, y: Y_test})))
    #print(np.shape(X_test))
    sess.close()