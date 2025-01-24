import argparse
import subprocess
import os

import validation_test as vt
from validation_test.utils.parse_json import parse_json

parser = argparse.ArgumentParser(description="SPH automated validation")
parser.add_argument("--json_pth", type=str, default="./sample.json", help="Path to the json file")

args = parser.parse_args()

json_pth = args.json_pth

data, json_list = parse_json(json_pth)

solver_pth = data["solver_pth"]
val_folder_pth = data["val_folder_pth"]
settings = data["settings"]
log_pth = data["log_pth"]

for j in json_list:
    argument = os.path.join(val_folder_pth, j) # i.e. "some_path/VAL_Hydro_Static.json"
    file_name = os.path.splitext(j)[0] # i.e. "VAL_Hydro_Static"
    save_log_pth = os.path.join(log_pth, file_name) # i.e. "log_path/VAL_Hydro_Static"
    
    if not os.path.exists(save_log_pth):
        os.makedirs(save_log_pth)

    with open(os.path.join(save_log_pth, 'log.txt'), 'w') as output_file:
        process = subprocess.Popen([solver_pth, argument], stdout=output_file, stderr=subprocess.STDOUT)
        process.communicate()
    
    result_pth = os.path.join(val_folder_pth, file_name) # i.e. "validation_path/VAL_Hydro_Static"
    function_name = f"vt.{file_name}"
    if function_name in globals():
        print(f"{function_name} is being executed...")
        globals()[function_name]()  # Call the function dynamically
    else:
        print(f"The function {function_name} is not defined.")    