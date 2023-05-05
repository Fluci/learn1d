import json
import argparse
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('paths', nargs='+', help='Paths to JSON files holding "data" field with "x" and "y" lists')
parser.add_argument('--out_plot', default='plot.png', help='Output file path for plot image')
parser.add_argument('--point_size', type=float, default=0.1, help='Size of each point in the plot')
args = parser.parse_args()

colors = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black']  # Set of colors to use for each file

scale = 4

fig, ax = plt.subplots(figsize=(scale * 6.4, scale * 4.8), dpi=400)
for i, path in enumerate(args.paths):
    with open(path) as f:
        data = json.load(f)['data']
    x, y = data['x'], data['y']
    ax.scatter(x, y, s=args.point_size, color=colors[i % len(colors)], label=path)

ax.legend()
plt.savefig(args.out_plot)
