import os
import matplotlib.pyplot as plt

from validation_test.utils.clip_and_extract import clip_and_extract
from validation_test.utils.dambbreak_result import (
    Ex_p1_time,
    Ex_p1_pressure,
    FVM_p1_time,
    FVM_p1_pressure,
    Ex_p3_time,
    Ex_p3_pressure,
    FVM_p3_time,
    FVM_p3_pressure
)

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
    
    plt.figure(figsize=(8, 6))
    plt.plot(times, mean_values[0], label="NFLOW SDK, p1", color='red')
    plt.plot(times_to_steps(Ex_p1_time), Ex_p1_pressure, label="Experiment", color='black')
    plt.plot(times_to_steps(FVM_p1_time), FVM_p1_pressure, label="FVM", color='blue')
    plt.xlabel("Steps")
    plt.ylabel(f"{data_array_name} {data_unit}")
    plt.legend(loc='upper right')
    plt.savefig(os.path.join(save_log_pth, "graph_p1.png"))
    
    plt.figure(figsize=(8, 6))
    plt.plot(times, mean_values[1], label="NFLOW SDK, p3", color='red')
    plt.plot(times_to_steps(Ex_p3_time), Ex_p3_pressure, label="Experiment", color='black')
    plt.plot(times_to_steps(FVM_p3_time), FVM_p3_pressure, label="FVM", color='blue')
    plt.xlabel("Steps")
    plt.ylabel(f"{data_array_name} {data_unit}")
    plt.legend(loc='upper right')
    plt.savefig(os.path.join(save_log_pth, "graph_p3.png"))
    
    return None

def times_to_steps(times, dt=0.02):
    return [time / dt for time in times]