16:30

1
Write a script that:
- Reads in a json file. The json file contains a field "data". In "data" there are two other fields: "x" and "y".  Reading the file should result in a dictionary representing that structure.
- The file uses argparse. the path to the json file is the first argument and called "training_data". A second, optional argument "output_directory" can be given. If it is not passed, the current working directory is used.
- We then set up a tensorflow model called dimOne. The model has one input value which is a double. The model has an output value which is also a double. In-between we have ten hidden layers, fully connected. Each layer has 10 elements and consists of rectified linear units.
- Now, we train the model for "iterations=100000". 
- Any output is written in files in "output_directory".
- Once the model is trained, we store it.

-----------------------------

16:34

2
Write a script that:
- Reads in a json file. The json file contains a field "data". In "data" there are two other fields: "x" and "y".  Reading the file should result in a dictionary representing that structure.
- The file uses argparse. the path to the json file is the first argument and called "training_data". A second, optional argument "output_directory" can be given. If it is not passed, the current working directory is used.
- We then set up a tensorflow model called dimOne. The model has one input value which is a double. The model has an output value which is also a double. In-between we have ten hidden layers, fully connected. Each layer has 10 elements and consists of rectified linear units.
- Now, we train the model for "iterations=100000".
- Any output is written in files in "output_directory".
- Once the model is trained, we store it.
- After every 100 training iterations, we want to store a snapshot of the model.
- Make sure we can observe training using tensorboard.

------------------------------------

16:49

Write a script that:
- Reads in a json file. The json file contains a field "data". In "data" there are two other fields: "x" and "y".  Reading the file should result in a dictionary representing that structure.
- The file uses argparse. the path to the json file is the first argument and called "training_data". A second, optional argument "output_directory" can be given. If it is not passed, the current wor    king directory is used.
- We then set up a tensorflow model called dimOne. The model has one input value which is a double. The model has an output value which is also a double. In-between we have ten hidden layers, fully c    onnected. Each layer has 10 elements and consists of rectified linear units.
- Now, we train the model for "iterations=100000".
- Any output is written in files in "output_directory".
- Once the model is trained, we store it.
- After every 1000 training iterations, we want to store a snapshot of the model.
- Make sure we can observe training using tensorboard.
- Make sure it is easy to switch between gpu and cpu training.

