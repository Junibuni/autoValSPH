import os
import numpy as np
import matplotlib.pyplot as plt

from validation_test.utils.clip_and_extract import clip_and_extract

def run(vtk_folder, save_log_pth, grid_number):
    bounds =  [[-0.5, 0.5, 0.0, 0.02, -0.5, 0.5]]
    data_array_name =  "pressure"
                
    times, mean_values = clip_and_extract(
        vtk_folder=vtk_folder,
        grid_number=grid_number,
        bounds=bounds,
        data_array_name=data_array_name
    )
    
    data_unit = "pa"
    
    plt.figure(figsize=(8, 6))
    plt.plot(times, mean_values[0], label="NFLOW SDK", color='red')
    plt.plot(times, [9810] * len(times), label="Theoretical", color='black')
    plt.xlabel("Steps")
    plt.ylabel(f"{data_array_name} {data_unit}")
    plt.legend(loc='upper right')
    plt.savefig(os.path.join(save_log_pth, "graph.png"))
    
    error = abs(np.mean(mean_values[0][-max(1, len(times) // 10):]) - 9810) / 9810 * 100
    
    return error
