import os

import numpy as np
import matplotlib.pyplot as plt

from validation_test.utils.interpolate_and_plot_line import interpolate_and_plot_line

def run(vtk_folder, save_log_pth, grid_number):
    radius =  0.002,
    n_points =  1000,
    start_point =  np.array([0.5, -0.05, 0.0]),
    end_point =  np.array([0.5, 0.05, 0.0]),
    data_array_name =  "velocity",
    xyz =  "x"

    distances, values = interpolate_and_plot_line(
        vtk_folder=vtk_folder, 
        grid_number=grid_number, 
        start_point=start_point, 
        end_point=end_point, 
        n_points=n_points, 
        data_array_name=data_array_name, 
        radius=radius,
        xyz=xyz)
    
    data_unit = "m/s"
    
    theoretical = 4*1.5*(distances/0.1 - (distances/0.1)**2)
    plt.figure(figsize=(4, 3))
    plt.plot(distances, values, label="NFLOW SDK")
    plt.plot(distances, theoretical, label="Theoretical") # 색깔은?
    plt.xlabel("Displacement m")
    plt.ylabel(f"{data_array_name} {data_unit}")
    plt.legend(loc='upper right')
    plt.savefig(os.path.join(save_log_pth, "graph.png"))
    # 후처리 이후 save_log_pth에 결과 저장 (csv)