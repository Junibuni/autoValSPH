import os
import matplotlib.pyplot as plt

from validation_test.utils.clip_and_extract import clip_and_extract

def run(vtk_folder, save_log_pth, grid_number):
    bounds =  [-0.5, 0.5, 0.0, 0.02, -0.5, 0.5]
    data_array_name =  "pressure"
                
    times, mean_values = clip_and_extract(
        vtk_folder=vtk_folder,
        grid_number=grid_number,
        bounds=bounds,
        data_array_name=data_array_name
    )
    
    data_unit = "pa"
    
    plt.figure(figsize=(4, 3))
    plt.plot(times, mean_values, label="NFLOW SDK")
    plt.plot(times, [9810] * len(times), color='black', label="Theoretical") # 색깔은?
    plt.xlabel("Steps")
    plt.ylabel(f"{data_array_name} {data_unit}")
    plt.legend(loc='upper right')
    plt.savefig(os.path.join(save_log_pth, "graph.png"))
    
    # 후처리 이후 save_log_pth에 결과 저장 (csv)
