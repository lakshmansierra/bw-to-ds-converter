import os
from datetime import datetime, timezone
from typing import Optional
import hdbcli.dbapi as dbapi
from dotenv import load_dotenv
from fastapi import Request, WebSocket

load_dotenv()

schema_name = os.getenv("HANA_SCHEMA")

def get_hana_connection(print_schema: bool = False, table_names: Optional[list[str]] = None):
    """
    Establishes a HANA connection and optionally prints table schema & returns HANA connection object.
    
    Args:
        print_schema (bool, optional): If True, prints columns and data types of the table. Defaults to False.
        table_name (str, optional): Name of the table whose schema to print. Defaults to None.
    """  
    conn = dbapi.connect(
        address=os.getenv("HANA_HOST"),
        port=int(os.getenv("HANA_PORT")),
        user=os.getenv("HANA_USER"),
        password=os.getenv("HANA_PASSWORD")
    )
    for table_name in table_names:
        if print_schema and table_name:
            cursor = conn.cursor()
            query = f"""
                SELECT COLUMN_NAME, DATA_TYPE_NAME
                FROM TABLE_COLUMNS
                WHERE TABLE_NAME = '{table_name}' AND SCHEMA_NAME = '{schema_name}'
            """
            cursor.execute(query)
            rows = cursor.fetchall()
            cursor.close()
            
            print(f"🗂️ Schema for table {table_name}:")
            for col_name, data_type in rows:
                print(f"{col_name} : {data_type}")
    
    return conn


def get_db(request: Request):
    """
    Retrieve the HANA database connection from the FastAPI app state.

    Args:
        request (Request): The FastAPI HTTP request object containing the app state.

    Returns:
        hdbcli.dbapi.Connection: Active HANA database connection.
    """
    return request.app.state.db


def get_db_from_ws(websocket: WebSocket):
    """
    same object you stored in FastAPI lifespan: app.state.db
    """
    return websocket.app.state.db


# -----------------------------------------------------------------------------------------------