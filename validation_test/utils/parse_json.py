import json
import os

def parse_json(json_file_path):
    try:
        with open(json_file_path, "r", encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Error: File {json_file_path} not found.")
        data = None
    except json.JSONDecodeError:
        print(f"Error: Failed to parse JSON in {json_file_path}.")
        data = None

    if data:
        solver_pth = data["solver_pth"]
        val_folder_pth = data["val_folder_pth"]
        settings = data["settings"]
        log_pth = data["log_pth"]
        name = data["name"]
        git = data["commit_number"]
        
        if not log_pth:
            log_pth = "./log"

        if os.path.exists(log_pth):
            i = 1
            new_log_pth = f"{log_pth}({i})"
            while os.path.exists(new_log_pth):
                i += 1
                new_log_pth = f"{log_pth}({i})"
            log_pth = new_log_pth
            print(f"Log folder already exists, creating a new one at {log_pth}\n")
        else:
            print(f"Log folder created at {log_pth}\n")

        data["log_pth"] = log_pth
        os.makedirs(log_pth)

        json_files = [
            f + '.json' for f in settings.keys()
        ]

        print("Solver Path:", solver_pth)
        print("Validation Folder Path:", val_folder_pth)
        print("Log Path:", log_pth)
        print("Author:", name)
        print("Commit Number:", git)
        print("JSON Files:", json_files)
        print()
        return data, json_files