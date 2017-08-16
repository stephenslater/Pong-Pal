import os, logging
try:
	import tensorflow as tf
	from PIL import Image
	import numpy as np
	os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
except ImportError:
	logging.warning('Failed to import tensorflow. DO NOT USE STATUS OR NOTIFY COMMAND.')


def get_single_img(file_path):
	img = Image.open(file_path)
	width = img.size[0]
	height = img.size[1]
	pixels =  np.array([np.array(img).flatten()])
	return pixels, width*height*3

def eval_single_img(file_path):
	image,size = get_single_img(file_path)

	with tf.Graph().as_default():
		images_placeholder = tf.placeholder(tf.float32, shape=[None, size])
		labels_placeholder = tf.placeholder(tf.int64, shape=[None])

		# Define variables (these are the values we want to optimize)
		weights = tf.Variable(tf.zeros([size, 2]))
		biases = tf.Variable(tf.zeros([2]))
		logits = tf.matmul(images_placeholder, weights) + biases
		correct_prediction = tf.equal(tf.argmax(logits, 1), labels_placeholder)

		saver = tf.train.Saver()

		with tf.Session() as sess:
			saver.restore(sess, "model/model.ckpt")
			res = sess.run(tf.argmax(logits, 1),feed_dict={images_placeholder: image})
			return res[0]	

if __name__ == '__main__':
	while True:
		path = raw_input("File Path: ")
		print(eval_single_img(path))
