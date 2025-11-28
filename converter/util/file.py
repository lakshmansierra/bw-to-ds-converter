import os,pandas as pd,json,re

def read_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
    
def write_json_file(json_file_path: str, content) -> None:
    try:
        with open(json_file_path, "w", encoding="utf-8") as f:
            json.dump(content, f, indent=4)
    except Exception as e:
        print(f"Exception in write_json_file: {e}")
        raise
    