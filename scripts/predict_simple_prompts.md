Write a script that:
- Loads a tensorflow model at path "trained_model".
- It also reads a file "test_data", by default "test_data.json".
- It also takes an argument "test_result" which is a path to an output json file.
- The json holds a field "data", which in turn holds two fields "x" and "y". Each is a list of numbers.
- The loaded model should be evaluated for each value in x. The results should be stored in y_predicted.
- "x" and "y_predicted" are stored in "test_result" in the fields "x" and "y", both fields of "data".


