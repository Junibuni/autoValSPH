import numpy as np

from validation_test.utils.interpolate_and_plot_line import interpolate_and_plot_line

def run(vtk_folder, save_log_pth, grid_number, start_point, end_point, n_points, data_array_name, radius):
    start_point = np.array(start_point)
    end_point = np.array(end_point)

    interpolate_and_plot_line(vtk_folder, grid_number, start_point, end_point, n_points, data_array_name, radius)
    
    # 후처리 이후 save_log_pth에 결과 저장 (csv)