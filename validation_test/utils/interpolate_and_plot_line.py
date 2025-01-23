import pyvista as pv
import numpy as np
import matplotlib.pyplot as plt
import os
import re

def wendland_quintic_kernel(r, h):
    alpha_d = 21 / (16 * np.pi * h**3)
    qm = max(1-r*0.5, 0)
    
    return alpha_d * (qm)**4 * (2 * r + 1)

def sph_interpolation_with_shepard(data, positions, start_point, end_point, n_points, radius):
    line_points = np.linspace(start_point, end_point, n_points)
    interpolated_values = []
    vol = radius ** 3
    smoothing_length = 4.8 * radius
    
    for point in line_points:
        weighted_sum = 0
        weight_total = 0

        for particle_pos, particle_val in zip(positions, data):
            distance = np.linalg.norm(particle_pos - point)
            if distance < smoothing_length:
                weight = wendland_quintic_kernel(distance, smoothing_length)
                weighted_sum += weight * particle_val * vol
                weight_total += weight * vol

        interpolated_values.append(weighted_sum / weight_total if weight_total > 0 else weighted_sum)

    distances = np.linspace(0, np.linalg.norm(end_point - start_point), n_points)
    return distances, interpolated_values

def interpolate_and_plot_line(vtk_folder, grid_number, start_point, end_point, n_points, data_array_name, radius):
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
    velocity_data = dataset[data_array_name]

    velocity_x = velocity_data[:, 0]

    distances, normalized_values = sph_interpolation_with_shepard(velocity_x, positions, start_point, end_point, n_points, radius)

    plt.plot(distances, normalized_values, label=f"SPH Interpolation (Grid {grid_number}, Time Step {last_time_index})")
    plt.xlabel("Distance Along Line")
    plt.ylabel("Normalized Velocity X")
    plt.title(f"SPH Interpolation of Velocity X Over Line (Grid {grid_number}, Time Step {last_time_index})")
    plt.legend()
    plt.grid()
    plt.show()