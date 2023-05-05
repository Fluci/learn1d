import argparse
import json
import os
import tensorflow as tf


def build_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(10, activation='relu'),
        tf.keras.layers.Dense(10, activation='relu'),
        tf.keras.layers.Dense(10, activation='relu'),
        tf.keras.layers.Dense(10, activation='relu'),
        tf.keras.layers.Dense(10, activation='relu'),
        tf.keras.layers.Dense(10, activation='relu'),
        tf.keras.layers.Dense(10, activation='relu'),
        tf.keras.layers.Dense(10, activation='relu'),
        tf.keras.layers.Dense(10, activation='relu'),
        tf.keras.layers.Dense(1)
    ])
    return model


def train_model(x, y, output_dir, iterations, device):
    os.makedirs(output_dir, exist_ok=True)
    tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=output_dir, histogram_freq=1)
    checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
        filepath=os.path.join(output_dir, "model_{epoch:03d}.h5"),
        save_freq=1000
    )
    model = build_model()
    if device == "gpu":
        physical_devices = tf.config.list_physical_devices('GPU')
        tf.config.experimental.set_memory_growth(physical_devices[0], True)
    elif device == "cpu":
        os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
    else:
        raise ValueError("Device must be 'gpu' or 'cpu'.")
    model.compile(optimizer='adam', loss='mse')
    x = tf.reshape(x, (-1, 1))
    model.fit(x, y, epochs=iterations, callbacks=[tensorboard_callback, checkpoint_callback])


def main(training_data, output_directory=None, iterations=100000, device="cpu"):
    with open(training_data, 'r') as f:
        data = json.load(f)
    x = data['data']['x']
    y = data['data']['y']
    output_directory = output_directory or os.getcwd()
    train_model(x, y, output_directory, iterations, device)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('training_data', type=str, default="training_data.json", help='path to json training data file')
    parser.add_argument('--output_directory', type=str, help='directory to store output files')
    parser.add_argument('--iterations', type=int, default=100000, help='number of iterations to train the model')
    parser.add_argument('--device', type=str, default="cpu", choices=["gpu", "cpu"], help='device to use for training')
    args = parser.parse_args()
    main(args.training_data, args.output_directory, args.iterations, args.device)
