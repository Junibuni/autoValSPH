import pyvista as pv
import numpy as np
import matplotlib.pyplot as plt
import os
import re

def wendland_quintic_kernel(r, h):
    alpha_d = 21 / (16 * np.pi * h**3)
    qm = np.maximum(1-r*0.5, 0)
    
    return alpha_d * (qm)**4 * (2 * r + 1)

def sph_interpolation_with_shepard(data, positions, start_point, end_point, n_points, radius):
    line_points = np.linspace(start_point, end_point, n_points)  # Shape: (n_points, 3)
    vol = radius ** 3
    smoothing_length = 4.8 * radius

    distances = np.linalg.norm(positions[:, None, :] - line_points[None, :, :], axis=-1)  # Shape: (num_particles, n_points)
    
    weights = np.where(distances < smoothing_length, 
                       wendland_quintic_kernel(distances, smoothing_length), 
                       0)  # Shape: (num_particles, n_points)

    weighted_values = (weights * data[:, None] * vol).sum(axis=0)  # Shape: (n_points,)
    weight_totals = (weights * vol).sum(axis=0)  # Shape: (n_points,)

    interpolated_values = np.where(weight_totals > 0, weighted_values / weight_totals, weighted_values)

    distances_output = np.linspace(0, np.linalg.norm(end_point - start_point), n_points)
    
    return distances_output, interpolated_values

def interpolate_and_plot_line(vtk_folder, grid_number, start_point, end_point, n_points, data_array_name, radius, xyz=None):
    def filter_and_extract_time(filename, grid_number):
        match = re.search(rf'grid{grid_number}_(\d+)\.vtk', filename)
        if match:
            return int(match.group(1))
        return None

    vtk_files = []
    for f in os.listdir(vtk_folder):
        if f.endswith('.vtk'):
            time_index = filter_and_extract_time(f, grid_number)
            if time_index is not None:
                vtk_files.append((os.path.join(vtk_folder, f), time_index))

    vtk_files.sort(key=lambda x: x[1])

    if not vtk_files:
        raise FileNotFoundError(f"No VTK files found for grid number {grid_number} in {vtk_folder}")

    last_file_path, last_time_index = vtk_files[-1]

    dataset = pv.read(last_file_path)

    positions = dataset.points
    if data_array_name not in dataset.array_names:
        raise ValueError(f"Data array '{data_array_name}' not found in the dataset.")
    
    data = np.array(dataset[data_array_name])

    # 3차원일 경우 extract
    if xyz:
        assert data.ndim == 2 and data.shape[1] == 3
        if xyz == 'x':
            data = data[:, 0]
        elif xyz == 'y':
            data = data[:, 1]
        elif xyz == 'z':
            data = data[:, 2]
        else:
            raise ValueError(f"Unknown variable: {xyz}")

    distances, values = sph_interpolation_with_shepard(data, positions, start_point, end_point, n_points, radius)

    # plt.plot(distances, values, label=f"SPH Interpolation (Grid {grid_number}, Time Step {last_time_index})")
    # plt.xlabel("Distance Along Line")
    # plt.ylabel("Normalized Velocity X")
    # plt.title(f"SPH Interpolation of Velocity X Over Line (Grid {grid_number}, Time Step {last_time_index})")
    # plt.legend()
    # plt.grid()
    # plt.show()
    return distances, values