import os, csv, json
from datetime import datetime

def generate_csv_folder_path(file_name: str) -> str:
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    base_dir = os.path.join(project_root, "repositories", "csv_repos")
    ts = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    print(f"ts: {ts}")

    dest_path = os.path.join(base_dir, f"{file_name}_{ts}")
    os.makedirs(dest_path, exist_ok=True)
    return os.path.normpath(dest_path)

def generate_json_folder_path(file_name: str) -> str:
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    base_dir = os.path.join(project_root, "repositories", "json_repos")
    ts = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    print(f"ts: {ts}")

    dest_path = os.path.join(base_dir, f"{file_name}_{ts}")
    os.makedirs(dest_path, exist_ok=True)
    return os.path.normpath(dest_path)

# ---------------------------------------

def generate_csv_file_path(csv_folder_path, file_name_with_csv):
    os.makedirs(csv_folder_path, exist_ok=True)
    csv_file_path = os.path.join(csv_folder_path, file_name_with_csv)
    return csv_file_path

def write_csv_file(csv_file_path: str, content) -> None:
    try:
        with open(csv_file_path, "wb") as f:
            f.write(content)
    except Exception as e:
        print(f"Exception in write_csv_file: {e}")
        raise

# ---------------------------------------

def generate_json_file_path(json_folder_path, file_name_with_json):
    os.makedirs(json_folder_path, exist_ok=True)
    json_file_path = os.path.join(json_folder_path, file_name_with_json)
    return json_file_path

def write_json_file(json_file_path: str, content) -> None:
    try:
        with open(json_file_path, "w", encoding="utf-8") as f:
            json.dump(content, f, indent=4)
    except Exception as e:
        print(f"Exception in write_json_file: {e}")
        raise

# ---------------------------------------

def csv_to_2d_list(csv_file_path: str):
    rows = []
    with open(csv_file_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            rows.append(row)
    return rows

def json_file_name_generator(file_name_with_csv):
    base_name, _ = os.path.splitext(file_name_with_csv)
    file_name_with_json = f"{base_name}.json"
    return file_name_with_json

def read_json_file(json_file_path: str) -> str:
    try:
        with open(json_file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = json.load(f)
        
    except Exception as e:
        print(f"Exception in read_json_file function: {e}")
        content = ""
    
    finally:
        return content