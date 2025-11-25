import os
from datetime import date, datetime, timezone
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


def insert_file_record(
                        conn,
                        *,
                        csv: str,
                        date: date,
                        csv_path: str,
                        json_path: str,
                        state: int
                    ) -> int:
    """
    Inserts a row into file_bw_to_ds table and returns the inserted id.
    """
    cursor = conn.cursor()
    try:
        query = f'''
            INSERT INTO "{schema_name}"."file_bw_to_ds"
              ("csv","date","csv_path","json_path","state")
            VALUES (?,?,?,?,?)
        '''
        cursor.execute(query, [csv, date, csv_path, json_path, int(state)])
        conn.commit()

        # Retrieve inserted ID based on unique csv_path (timestamp inside path)
        sel = f'''
            SELECT A."id"
            FROM "{schema_name}"."file_bw_to_ds" A
            WHERE A."csv_path" = ?
            ORDER BY A."id" DESC
            LIMIT 1
        '''
        cursor.execute(sel, [csv_path])
        row = cursor.fetchone()
        print("👉", row)

        # Close connection
        cursor.close()
        if row is None:
            raise Exception("Insert succeeded but could not retrieve inserted id")
        
        row_val = row[0]
        return int(row_val)

    except Exception as e:
        raise


def insert_initial_conversion_run_status(conn, file_id: int) -> int:
    """
    Inserts a row into conversion_run_status_neo_to_cf with status=0 for the given file_id.
    Returns the inserted id.
    """
    cursor = conn.cursor()
    try:
        ins = f'''
            INSERT INTO "{schema_name}"."conversion_run_status_bw_to_ds"
                ("file_id","conversion_run_status")
            VALUES (?, 0)
        '''
        cursor.execute(ins, [int(file_id)])
        conn.commit()

        # Fetch the row we just inserted 
        sel = f'''
            SELECT "id", "file_id", "conversion_run_status"
            FROM "{schema_name}"."conversion_run_status_bw_to_ds"
            WHERE "file_id" = ?
            ORDER BY "id" DESC
            LIMIT 1
        '''
        cursor.execute(sel, [int(file_id)])
        row = cursor.fetchone()
        print("👉", row)

        # Close connection
        cursor.close()
        if row is None:
            raise Exception("Insert into conversion_run_status_bw_to_ds succeeded but could not retrieve inserted id")
        
        row_val = row[0]
        return int(row_val)

    except Exception as e:
        raise