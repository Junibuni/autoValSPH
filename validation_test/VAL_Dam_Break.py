import os
import matplotlib.pyplot as plt

from validation_test.utils.clip_and_extract import clip_and_extract

def run(vtk_folder, save_log_pth, grid_number):
    bounds =  [-0.52, -0.48, 0.0, 0.04, -0.84, -0.82]
    data_array_name =  "pressure"
    
    times, mean_values = clip_and_extract(
        vtk_folder=vtk_folder,
        grid_number=grid_number,
        bounds=bounds,
        data_array_name=data_array_name
    )
    
    data_unit = "pa"
    
    plt.figure(figsize=(4, 3))
    plt.plot(times, mean_values, label="NFLOW SDK, p1")
    plt.xlabel("Steps")
    plt.ylabel(f"{data_array_name} {data_unit}")
    plt.legend(loc='upper right')
    plt.savefig(os.path.join(save_log_pth, "graph_p1.png"))
    
"""    plt.figure(figsize=(4, 3))
    plt.plot(times, mean_values, label="NFLOW SDK, p3")
    plt.xlabel("Steps")
    plt.ylabel(f"{data_array_name} {data_unit}")
    plt.legend(loc='upper right')
    plt.savefig(os.path.join(save_log_pth, "graph_p1.png"))"""
    #p1 p3 에 대해 fvm, experiment 와 비교 필요
    # 후처리 이후 save_log_pth에 결과 저장 (csv)