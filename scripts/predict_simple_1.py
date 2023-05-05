import argparse
import json
import tensorflow as tf

def load_model(model_path):
    return tf.keras.models.load_model(model_path)

def evaluate_model(model, x):
    y_predicted = model.predict(x)
    return y_predicted

def main(model_path, test_data_path="test_data.json", test_result_path="test_result.json"):
    # Load model
    model = load_model(model_path)

    # Load test data
    with open(test_data_path, 'r') as f:
        test_data = json.load(f)
    x = test_data['data']['x']

    # Evaluate model
    y_predicted = evaluate_model(model, x)

    # Save test results
    test_result = {'data': {'x': x, 'y': y_predicted.tolist()}}
    with open(test_result_path, 'w') as f:
        json.dump(test_result, f)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('model_path', type=str, help='path to trained TensorFlow model')
    parser.add_argument('--test_data_path', type=str, default='test_data.json', help='path to test data JSON file')
    parser.add_argument('--test_result_path', type=str, default='test_result.json', help='path to test result JSON file')
    args = parser.parse_args()

    main(args.model_path, args.test_data_path, args.test_result_path)
