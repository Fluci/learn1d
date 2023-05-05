Create a python script that:
- has a lambda dimOneFn, defined later by the user. It takes one double as input and returns one double.
- The script uses argparse. Arguments are a path "out_filename" which will be a json file. An optional integer argument called "samples_count", default being 1000. An optional float "range_start", default 0.0. An optional float "range_end", default 1.0.
- The script creates "samples_count" random values in the range between "range_start" and "range_end". We'll call this list "xs"
- Each element in "xs" is passed to the lambda dimOneFn and stored in a list called "ys".
- Finally, a json file is wirtten at "out_filename". The json file contains a field "data" whch in turn holds a field "x" (holding the values of "xs") and "y" (holding the values of "ys"). Next to "data", we also store "samples_count" and "range". The range is a tuple of range_start and range_end.
- Store the seed used for the random number generator as well.
