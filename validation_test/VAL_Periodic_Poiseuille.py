import numpy as np
import matplotlib.pyplot as plt

from validation_test.utils.interpolate_and_plot_line import interpolate_and_plot_line

def run(vtk_folder, save_log_pth, grid_number):
    radius = 0.01,
    n_points = 1000,
    start_point = np.array([0.5, -0.5, 0.0]),
    end_point = np.array([0.5, 0.5, 0.0]),
    data_array_name = "velocity",
    xyz = "x"

    distances, values = interpolate_and_plot_line(
        vtk_folder=vtk_folder, 
        grid_number=grid_number, 
        start_point=start_point, 
        end_point=end_point, 
        n_points=n_points, 
        data_array_name=data_array_name, 
        radius=radius,
        xyz=xyz)
    
    plt.figure(figsize=(4, 3))
    plt.plot(distances, values, label=f"SPH Interpolation (Grid {grid_number}, Time Step {last_time_index})")
    plt.xlabel("Distance Along Line")
    plt.ylabel("Normalized Velocity X")
    plt.title(f"SPH Interpolation of Velocity X Over Line (Grid {grid_number}, Time Step {last_time_index})")
    plt.legend()
    plt.grid()
    plt.show()
    
    # 후처리 이후 save_log_pth에 결과 저장 (csv)