import numpy as np

from validation_test.utils.interpolate_and_plot_line import interpolate_and_plot_line

def run(vtk_folder, n_points=100):
    grid_number = 1
    radius = 0.01
    start_point = np.array([0.5, -0.5, 0.0])
    end_point = np.array([0.5, 0.5, 0.0])
    data_array_name = "velocity"

    interpolate_and_plot_line(vtk_folder, grid_number, start_point, end_point, n_points, data_array_name, radius)