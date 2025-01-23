import argparse
import subprocess
import os
import validation_test as vt

# parser = argparse.ArgumentParser(description="SPH automated validation")
# parser.add_argument("source_folder", help="Path to the source folder")

# args = parser.parse_args()

# source_pth = args.source_folder

#vt.hydrostatic(r"D:\WorkSpace\001solver\000SDK_3D\sources\test_files\Validation\VAL_Hydro_Static")
#vt.dambreak(r"D:\WorkSpace\001solver\000SDK_3D\sources\test_files\Validation\VAL_Dam_Break")
#vt.periodic_poiseulle(r"D:\WorkSpace\001solver\000SDK_3D\sources\test_files\SPH\periodic_poiseuille")
#vt.obc_poiseuille(r"D:\WorkSpace\001solver\000SDK_3D\sources\test_files\SPH\periodic_poiseuille")


# exe_path = os.path.join(source_pth, r"\VSBuild\x64\Release\RuntimeSPH.exe")

# json_list = [
#     "VAL_Hydro_Static.json",
#     "VAL_Dam_Break.json",
#     "VAL_Periodic_Poiseuille.json",
#     "VAL_OBC_Poiseuille.json",
# ]

# for test in json_list:
#     argument = os.path.join(source_pth, r"\test_files\Validation\VAL_Periodic_Poiseuille.json")


# # Open a file to write the output
# with open('output.txt', 'w') as output_file:
#     process = subprocess.Popen([exe_path, argument], stdout=output_file, stderr=subprocess.STDOUT)
#     process.communicate()
    
vt.periodic_poiseulle(r"D:\WorkSpace\001solver\000SDK_3D\sources\test_files\Validation\VAL_Periodic_Poiseuille")