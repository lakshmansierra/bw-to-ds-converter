import json, os,re
import pandas as pd
from .llm.models_llm import converter_llm
from .util.file import write_json_file
from .prompt.csv_sample1 import csv_sample1
from .prompt.csv_sample2 import csv_sample2
from .prompt.csv_sample3 import csv_sample3
from .prompt.CDS_JSON_PROMPT import CDS_JSON_PROMPT

import json
import requests
from dotenv import load_dotenv
from langchain_core.load import dumps as lc_dumps

from .prompt.json1 import json1
from .prompt.json2 import json2
from .prompt.json3 import json3

from langchain.prompts import PromptTemplate

load_dotenv()
LLM_USAGE_MONITOR_APP_ID = os.getenv("LLM_USAGE_MONITOR_APP_ID")
LLM_USAGE_MONITOR_MODEL_NAME = os.getenv("LLM_USAGE_MONITOR_MODEL_NAME")
LLM_USAGE_MONITOR_API_KEY = os.getenv("LLM_USAGE_MONITOR_API_KEY")
LLM_USAGE_MONITOR_BASE_URL = os.getenv("LLM_USAGE_MONITOR_BASE_URL")
LLM_USAGE_MONITOR_CALL_TYPE_L_INVOKE = os.getenv("LLM_USAGE_MONITOR_CALL_TYPE_L_INVOKE")
LLM_USAGE_MONITOR_CALL_TYPE_A_INVOKE = os.getenv("LLM_USAGE_MONITOR_CALL_TYPE_A_INVOKE")

LLM_USAGE_MONITOR_FULL_URL = f"{LLM_USAGE_MONITOR_BASE_URL}/log-metadata/?app_id={LLM_USAGE_MONITOR_APP_ID}&call_type={LLM_USAGE_MONITOR_CALL_TYPE_L_INVOKE}&model_name={LLM_USAGE_MONITOR_MODEL_NAME}"
LLM_USAGE_MONITOR_BEARER_TOKEN = f"Bearer {LLM_USAGE_MONITOR_API_KEY}"

def run_pipeline(csv_file_path, json_file_path):
    df = pd.read_csv(csv_file_path)
    csv_input = df.to_string(index=False)
    llm = converter_llm
    
    
    prompt_template=PromptTemplate(
        input_variables=[
            "csv_input",
            "csv_sample1", "json1",
            "csv_sample2", "json2",
            "csv_sample3", "json3"
        ],
        template=CDS_JSON_PROMPT
    )
    
    chain = prompt_template | llm
    response = chain.invoke({
        "csv_input": csv_input,
        "csv_sample1": csv_sample1,
        "json1": json1,
        "csv_sample2": csv_sample2,
        "json2": json2,
        "csv_sample3": csv_sample3,
        "json3": json3
    })

    payload = {
    "metadata": json.dumps(response.model_dump(), default=str)
    }

    headers = {
        "Authorization": LLM_USAGE_MONITOR_BEARER_TOKEN,
        "Content-Type": "application/json"
    }

    http_response = requests.post(LLM_USAGE_MONITOR_FULL_URL, json=payload, headers=headers)

    raw_content = getattr(response, "content", '{}')        
    # print(f"0----------> {type(raw_content)}")
    
    raw_content = re.sub(
        r'"expression"\s*:\s*""(.*?)""',
        r'"expression": "\"\1\""', 
        raw_content
    )
    # print(f"1----------> {type(raw_content)}")

    raw_content = re.sub(
    r'("expression"\s*:\s*".*?\()"?([^"]+)"?(\))',
    r'\1\"\2\"\3',
    raw_content
    )
    # print(f"2----------> {type(raw_content)}")

    parsed = json.loads(raw_content)
    # print(f"----------> {type(parsed)}")

    print(raw_content)
    try:
        write_json_file(json_file_path=json_file_path, content=parsed)
        
        
    except Exception as e:
        print(f"--->LLM output is not valid JSON: {e}")
        parsed = {}
        write_json_file(json_file_path=json_file_path, content=parsed)

    finally:
        return parsed
