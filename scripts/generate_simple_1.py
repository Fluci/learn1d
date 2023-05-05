import argparse
import json
import random
import numpy as np
import math


# Change Here:

#dimOneFn = lambda x: x**2
dimOneFn = lambda x: math.sin(x)



# Define the command-line arguments
parser = argparse.ArgumentParser(description='Generate and evaluate samples using a lambda function')
parser.add_argument('out_filename', type=str, help='the output filename (JSON)')
parser.add_argument('--samples_count', type=int, default=1000, help='number of samples to generate (default: 1000)')
parser.add_argument('--range_start', type=float, default=0.0, help='start of the range (default: 0.0)')
parser.add_argument('--range_end', type=float, default=1.0, help='end of the range (default: 1.0)')
parser.add_argument('--sample-strategy', type=str, default='random', help='random,linspace')

# Parse the command-line arguments
args = parser.parse_args()

seed = random.randint(0, 2**32 - 1)
if args.sample_strategy == 'random':
    # Set up the random number generator
    random.seed(seed)

    # Generate the samples
    xs = [random.uniform(args.range_start, args.range_end) for _ in range(args.samples_count)]
elif args.sample_strategy == 'linspace':
    xs = np.linspace(args.range_start, args.range_end, num=args.samples_count).tolist()
else:
    raise ValueError("Sample strategy must be in: random,linspace")

ys = [dimOneFn(x) for x in xs]

# Prepare the output dictionary
output = {
    'data': {'x': xs, 'y': ys},
    'samples_count': args.samples_count,
    'range': (args.range_start, args.range_end),
    'random_seed': seed,
    'sample_strategy': args.sample_strategy
}

# Write the output to a JSON file
with open(args.out_filename, 'w') as f:
    json.dump(output, f)

