import argparse
import json
import matplotlib.pyplot as plt


def plot_point_clouds(files, out_plot="plot.png"):
    fig, ax = plt.subplots()

    # Plot each point cloud with a different color
    for i, file in enumerate(files):
        with open(file) as f:
            data = json.load(f)["data"]
            x = data["x"]
            y = data["y"]
            ax.scatter(x, y, label=f"Point Cloud {i+1}")

    ax.legend()
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title("Point Clouds")
    plt.savefig(out_plot)
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="+", help="List of JSON files")
    parser.add_argument(
        "--out_plot",
        default="plot.png",
        help="Output filename for the plot (default: plot.png)",
    )
    args = parser.parse_args()

    plot_point_clouds(args.files, args.out_plot)
