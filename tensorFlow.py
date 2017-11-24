import tensorflow as tf


# x = tf.constant([35, 40, 45],name='x')
# y = tf.Variable(x + [10, 15, 20], name='y')
#
# model = tf.global_variables_initializer()
# with tf.Session() as session:
#     session.run(model)
#     print(session.run(y))


# import numpy as np
# # data = np.random.randint(1000, size=10000)
#
# x = tf.constant(np.random.randint(1000, size=10000), name='x')
# y = tf.Variable(( (5*(x**2)) - (3*x) + 15 ), name='y')
#
# # y = ( (5*(x**2)) - (3*x) + 15 )
#
# model = tf.global_variables_initializer()
# with tf.Session() as session:
#     session.run(model)
#     print(session.run(y))

# x = tf.Variable(0, name='x')
#
# model = tf.global_variables_initializer()
#
# with tf.Session() as session:
#     session.run(model)
#     for i in range(10):
#         x = x + i
#         print(session.run(x))

import tensorflow as tf

x = tf.constant(35, name='x')
print(x)
y = tf.Variable(x + 5, name='y')

with tf.Session() as session:
    merged = tf.summary.merge_all()
    writer = tf.summary.FileWriter("/tmp/basic", session.graph)
    model =  tf.global_variables_initializer()
    session.run(model)
    print(session.run(y))