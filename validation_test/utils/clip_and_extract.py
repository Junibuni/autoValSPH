import os
import re

import pyvista as pv
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

def clip_and_extract(vtk_folder, grid_number, bounds, data_array_name):
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

    mean_values_by_bound = {i: [] for i in range(len(bounds))}
    times = []
    
    for file_path, time_index in tqdm(vtk_files):
        dataset = pv.read(file_path)
        
        for i, bound in enumerate(bounds):
            clipped = dataset.clip_box(bound)
            
            if data_array_name in clipped.array_names:
                data = clipped[data_array_name]
                mean_values_by_bound[i].append(data.mean())
                times.append(time_index)
            else:
                print(f"Array '{data_array_name}' not found in {file_path}")

    # plt.figure()
    # plt.plot(times, mean_values, marker='o', label=f"Grid {grid_number}")
    # plt.xlabel("Time Step")
    # plt.ylabel(f"Mean Value of {data_array_name}")
    # plt.title(f"Clipped Data Over Time for Grid {grid_number}")
    # plt.legend()
    # plt.grid()
    # plt.show()
    return times, mean_values_by_bound