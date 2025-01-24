import numpy as np

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
    
    # 후처리 이후 save_log_pth에 결과 저장 (csv)