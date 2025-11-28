import json, os,re
import pandas as pd
from .llm.models_llm import converter_llm
from .util.file import write_json_file
from .prompt.csv_sample1 import csv_sample1
from .prompt.csv_sample2 import csv_sample2
from .prompt.csv_sample3 import csv_sample3
from .prompt.CDS_JSON_PROMPT import CDS_JSON_PROMPT

from .prompt.json1 import json1
from .prompt.json2 import json2
from .prompt.json3 import json3

from langchain.prompts import PromptTemplate

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
    raw_content = getattr(response, "content", '{}')        
    
    
    raw_content = re.sub(
        r'"expression"\s*:\s*""(.*?)""',
        r'"expression": "\"\1\""', 
        raw_content
    )
  
    raw_content = re.sub(
    r'("expression"\s*:\s*".*?\()"?([^"]+)"?(\))',
    r'\1\"\2\"\3',
    raw_content
)
    parsed = raw_content
    print(raw_content)
    try:
        write_json_file(json_file_path=json_file_path, content=parsed)
        
        
    except Exception as e:
        print(f"--->LLM output is not valid JSON: {e}")
        parsed = {}
        write_json_file(json_file_path=json_file_path, content=parsed)

    finally:
        return parsed
