# Simple Neural Network to classify handwritten digits from MNIST dataset
import tensorflow as tf 
from tensorflow.examples.tutorials.mnist import input_data

# We use the TF helper function to pull down the data from the MNIST site
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

