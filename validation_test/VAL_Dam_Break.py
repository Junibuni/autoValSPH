import os
import matplotlib.pyplot as plt
import pandas as pd

from validation_test.utils.clip_and_extract import clip_and_extract

def run(vtk_folder, save_log_pth, grid_number):
    bounds =  [[-0.52, -0.48, 0.0, 0.04, -0.84, -0.82],
               [-0.52, -0.48, 0.08, 0.12, -0.84, -0.82]]
    data_array_name =  "pressure"
    
    times, mean_values = clip_and_extract(
        vtk_folder=vtk_folder,
        grid_number=grid_number,
        bounds=bounds,
        data_array_name=data_array_name
    )
    
    data_unit = "pa"
    
    ref_data = get_ref_values()
    plt.figure(figsize=(4, 3))
    plt.plot(times, mean_values[0], label="NFLOW SDK, p1", color='red')
    plt.plot(ref_data["p1_ex_time"], ref_data["p1_ex_pressure"], label="Experiment", color='black')
    plt.plot(ref_data["p1_fvm_time"], ref_data["p1_fvm_pressure"], label="FVM", color='blue')
    plt.xlabel("Steps")
    plt.ylabel(f"{data_array_name} {data_unit}")
    plt.legend(loc='upper right')
    plt.savefig(os.path.join(save_log_pth, "graph_p1.png"))
    
    plt.figure(figsize=(4, 3))
    plt.plot(times, mean_values[1], label="NFLOW SDK, p3", color='red')
    plt.plot(ref_data["p3_ex_time"], ref_data["p3_ex_pressure"], label="Experiment", color='black')
    plt.plot(ref_data["p3_fvm_time"], ref_data["p3_fvm_pressure"], label="FVM", color='blue')
    plt.xlabel("Steps")
    plt.ylabel(f"{data_array_name} {data_unit}")
    plt.legend(loc='upper right')
    plt.savefig(os.path.join(save_log_pth, "graph_p3.png"))

    
def get_ref_values():
    file_path = 'validation_test\utils\dambreak_ref.csv'
    data = pd.read_csv(file_path)
    
    data.columns = [
    "p1_ex_time", "p1_ex_pressure", "p1_fvm_time", "p1_fvm_pressure",
    "p3_ex_time", "p3_ex_pressure", "p3_fvm_time", "p3_fvm_pressure"
    ]

    cleaned_data = data.iloc[2:].reset_index(drop=True)

    cleaned_data = cleaned_data.apply(pd.to_numeric, errors='coerce')

    p1_ex_time = cleaned_data["p1_ex_time"].to_numpy()
    p1_ex_pressure = cleaned_data["p1_ex_pressure"].to_numpy()
    p1_fvm_time = cleaned_data["p1_fvm_time"].to_numpy()
    p1_fvm_pressure = cleaned_data["p1_fvm_pressure"].to_numpy()

    p3_ex_time = cleaned_data["p3_ex_time"].to_numpy()
    p3_ex_pressure = cleaned_data["p3_ex_pressure"].to_numpy()
    p3_fvm_time = cleaned_data["p3_fvm_time"].to_numpy()
    p3_fvm_pressure = cleaned_data["p3_fvm_pressure"].to_numpy()

    return{
        "p1_ex_time": p1_ex_time[:5],
        "p1_ex_pressure": p1_ex_pressure[:5],
        "p1_fvm_time": p1_fvm_time[:5],
        "p1_fvm_pressure": p1_fvm_pressure[:5],
        "p3_ex_time": p3_ex_time[:5],
        "p3_ex_pressure": p3_ex_pressure[:5],
        "p3_fvm_time": p3_fvm_time[:5],
        "p3_fvm_pressure": p3_fvm_pressure[:5],
    }
