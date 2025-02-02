import argparse
import subprocess
import os
import time

import importlib
from validation_test.utils.parse_json import parse_json
from validation_test.utils.save_report import Document

parser = argparse.ArgumentParser(description="SPH automated validation")
parser.add_argument("--json_pth", "-j", type=str, default="./sample.json", help="Path to the json file")

args = parser.parse_args()

json_pth = args.json_pth

data, json_list = parse_json(json_pth)

solver_pth = data["solver_pth"]
val_folder_pth = data["val_folder_pth"]
settings = data["settings"]
log_pth = data["log_pth"]

data_dict = dict()
doc = Document(save_pth=log_pth, name=data['name'], git=data['commit_number'])

for j in json_list:
    argument = os.path.join(val_folder_pth, j) # i.e. "some_path/VAL_Hydro_Static.json"
    file_name = os.path.splitext(j)[0] # i.e. "VAL_Hydro_Static"
    save_log_pth = os.path.join(log_pth, file_name) # i.e. "log_path/VAL_Hydro_Static"
    
    if not os.path.exists(save_log_pth):
        os.makedirs(save_log_pth)

    print()
    print("="*50)
    try:
        print(f"Executing program for: {file_name}")
        with open(os.path.join(save_log_pth, 'log.txt'), 'w') as output_file:
            print(f"Running command: {solver_pth} {argument}")
            start_time = time.time()
            process = subprocess.Popen([solver_pth, argument], stdout=output_file, stderr=subprocess.STDOUT)
            process.communicate()
            end_time = time.time()
            execution_time = end_time - start_time
            print(f"Execution Time: {execution_time:.2f}s")
            print(f"Program output is logged to: {save_log_pth}")
            print()
    except subprocess.CalledProcessError as e:
        print(f"Error during executing program for {file_name}. Check log file: {save_log_pth}")
        raise

    try:                    
        print(f"Post-processing VTK files for: {file_name}")
        result_pth = os.path.join(val_folder_pth, file_name) # i.e. "validation_path/VAL_Hydro_Static"
        module = importlib.import_module(f"validation_test.{file_name}")
        function_name = "run"
        if hasattr(module, function_name):
            error = getattr(module, function_name)(result_pth, save_log_pth, **settings[file_name])  
            print(f"Post-processing for {file_name} is finished.")
            print()
            doc.write_section(file_name, save_log_pth, execution_time, error)
        else:
            print(f"The function {module}.{function_name} is not defined.")  

    except subprocess.CalledProcessError as e:
        print(f"Error during post-processing for {file_name}.")
        raise
    
    print()
    
doc.save()