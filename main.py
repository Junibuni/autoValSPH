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
    argument = os.path.join(val_folder_pth, j)
    file_name = os.path.splitext(j)[0]
    save_log_pth = os.path.join(log_pth, file_name)
    
    if not os.path.exists(save_log_pth):
        os.makedirs(save_log_pth)

    with open(os.path.join(save_log_pth, 'log.txt'), 'w') as output_file:
        process = subprocess.Popen([solver_pth, argument], stdout=output_file, stderr=subprocess.STDOUT)
        process.communicate()
    
    result_pth = os.path.join(val_folder_pth, file_name)
    match file_name:
        case "VAL_Hydro_Static":
            vt.hydrostatic(result_pth, save_log_pth, **settings[file_name])
            
        case "VAL_Dam_Break":
            vt.dambreak(result_pth, save_log_pth, **settings[file_name])
            
        case "VAL_OBC_Poiseuille":
            vt.obc_poiseuille(result_pth, save_log_pth, **settings[file_name])
            
        case "VAL_Periodic_Poiseuille":
            vt.periodic_poiseulle(result_pth, save_log_pth, **settings[file_name])