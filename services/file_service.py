import os, shutil, time
from urllib.parse import urlparse
from datetime import datetime

def csv_file_path(file_name: str) -> str:
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    base_dir = os.path.join(project_root, "repositories", "csv_repos")
    os.makedirs(base_dir, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    print(f"ts: {ts}")

    dest_path = os.path.join(base_dir, f"{file_name}_{ts}")
    # os.makedirs(dest_path, exist_ok=True)
    return os.path.normpath(dest_path)

def json_file_path(file_name: str) -> str:
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    base_dir = os.path.join(project_root, "repositories", "json_repos")
    os.makedirs(base_dir, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    print(f"ts: {ts}")

    dest_path = os.path.join(base_dir, f"{file_name}_{ts}")
    # os.makedirs(dest_path, exist_ok=True)
    return os.path.normpath(dest_path)

def write_uploaded_file(csv_folder_path: str, content, file_name_with_csv) -> None:
    """
    Streams the uploaded file to disk without loading into memory.
    """
    try:
        os.makedirs(csv_folder_path, exist_ok=True)
        csv_full_path = os.path.join(csv_folder_path, file_name_with_csv)
        with open(csv_full_path, "wb") as f:
            f.write(content)
    except Exception as e:
        print(f"Exception in write_uploaded_file: {e}")
        raise
