Write a script that:
- takes a list of paths as its arguments (using argparse). There's an optional argument "out_plot", by default "plot.png"
- Each file must be a json file holding a field "data". Each data field has two sub fields "x" and "y". Both hold lists of numbers, representing coordinates of points.
- Each input file represents a 2d point cloud. The script creates a plot showing all of them. Each group has a different color.
- The plot is stored at "out_plot"


------------------

2
Write a script that:
- takes a list of paths as its arguments (using argparse). There's an optional argument "out_plot", by default "plot.png"
- Each file must be a json file holding a field "data". Each data field has two sub fields "x" and "y". Both hold lists of numbers, representing coordinates of points.
- Each input file represents a 2d point cloud. The script creates a plot showing all of them. Each group has a different color.
- The plot is stored at "out_plot"
- All points have a minimal size, as we expect many thousand of points.
