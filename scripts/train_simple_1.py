import argparse
import os
import json
import tensorflow as tf

# Define command line arguments
parser = argparse.ArgumentParser(description='Train a TensorFlow model using data from a JSON file')
parser.add_argument('training_data', type=str, help='Path to the JSON file containing training data')
parser.add_argument('--output_directory', type=str, default=os.getcwd(), help='Path to the output directory (default: current working directory)')
args = parser.parse_args()

# Load training data from JSON file
with open(args.training_data, 'r') as f:
    data_dict = json.load(f)
x_train = data_dict['data']['x']
y_train = data_dict['data']['y']

# Define TensorFlow model
dimOne = tf.keras.Sequential()
dimOne.add(tf.keras.layers.Dense(10, input_shape=(1,), activation='relu'))
for i in range(9):
    dimOne.add(tf.keras.layers.Dense(10, activation='relu'))
dimOne.add(tf.keras.layers.Dense(1, activation=None))

# Train the model
dimOne.compile(optimizer='adam', loss='mse')
dimOne.fit(x_train, y_train, epochs=100000, verbose=0)

# Save the model to the output directory
output_path = os.path.join(args.output_directory, 'dimOne')
dimOne.save(output_path)
