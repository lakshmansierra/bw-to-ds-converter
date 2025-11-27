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
    Inserts a row into conversion_run_status_bw_to_ds with status=0 for the given file_id.
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


def get_state(conn, id: int) -> dict:
    """
    0 = not started, 1 = converted.
    """
    cursor = conn.cursor()
    try:
        sel = f'''
            SELECT "id", "state", "csv"
            FROM "{schema_name}"."file_bw_to_ds"
            WHERE "id" = ?
            ORDER BY "id" DESC
            LIMIT 1
        '''
        cursor.execute(sel, [int(id)])
        row = cursor.fetchone()
        print("👉", row)

        # Close connection
        cursor.close()
        if not row:
            raise Exception(f"Could not retrieve inserted state for file_id {id}")
        
        row_val = {
            "file_id": row[0], 
            "state": row[1],
            "csv": row[2],
            }
        return row_val

    except Exception as e:
        raise


def get_all_run_status(conn, file_id: int) -> dict:
    """
    Returns both run-status flags for an file_id:
      { "conversion_run_status": 0|1|2 }
    Missing rows are treated as 0.
    """
    cursor = conn.cursor()
    try:
        q = f'''
            SELECT
                COALESCE(MRS."conversion_run_status", 0) AS conversion_run_status
            FROM "{schema_name}"."file_bw_to_ds" A
            LEFT JOIN "{schema_name}"."conversion_run_status_bw_to_ds" MRS
              ON MRS."file_id" = A."id"
            WHERE A."id" = ?
            LIMIT 1
        '''
        cursor.execute(q, [int(file_id)])
        row = cursor.fetchone()
        print("👉", row)

        # Close connection
        cursor.close()
        if not row:
            raise Exception(f"there is no row for this file_id {file_id}")
        
        row_val = {
            "conversion_run_status": int(row[0])
        }
        return row_val

    except Exception:
        raise


def get_file_paths_or_404(conn, file_id: int) -> tuple[str | None, str | None]:
    cursor = conn.cursor()
    try:
        query = f'''
            SELECT "csv_path", "json_path"
            FROM "{schema_name}"."file_bw_to_ds"
            WHERE "id" = ?
            ORDER BY "id" DESC
            LIMIT 1
        '''
        cursor.execute(query, [int(file_id)])
        row = cursor.fetchone()
        print("👉", row)

        # Close connection
        cursor.close()
        if row is None:
            raise Exception(f"file_id {file_id} not found")
        
        row_val = (row[0], row[1])
        return row_val

    except Exception as e:
        raise


def set_conversion_run_status(conn, file_id: int, status: int) -> None:
    """
    0 = not started, 1 = running, 2 = completed.
    """
    cursor = conn.cursor()
    try:
        upd = f'''
            UPDATE "{schema_name}"."conversion_run_status_bw_to_ds"
            SET "conversion_run_status" = ?
            WHERE "file_id" = ?
        '''
        cursor.execute(upd, [int(status), int(file_id)])
        conn.commit()

        # Close connection
        cursor.close()

    except Exception as e:
        raise


def _fmt_longdate(dt: datetime) -> str:
    """Return 'YYYY-MM-DD HH:MM:SS.fffffffff' (7 fractional digits) in UTC-like form."""
    # dt.utcnow() has microseconds (6). Pad a trailing zero to get 7 digits.
    # Example: 2025-10-13 10:00:00.000000 -> '2025-10-13 10:00:00.0000000'
    return dt.strftime("%Y-%m-%d %H:%M:%S.%f") + "0"


def insert_conversion_status(conn, file_id: int, start_ts: datetime, end_ts: datetime, status: int) -> tuple:
    """
    Inserts a row into conversion_status_bw_to_ds and returns the inserted id.
    status: 1 success, 0 failure
    """
    cursor = conn.cursor()
    try:
        ins = f'''
            INSERT INTO "{schema_name}"."conversion_status_bw_to_ds"
                ("file_id","start_time","end_time","conversion_status")
            VALUES (
                ?,
                CAST(? AS LONGDATE),
                CAST(? AS LONGDATE),
                ?
            )
        '''
        cursor.execute(ins, (int(file_id), _fmt_longdate(start_ts), _fmt_longdate(end_ts), int(status)))
        conn.commit()

        sel = f'''
            SELECT "id", "start_time", "end_time"
            FROM "{schema_name}"."conversion_status_bw_to_ds"
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
            raise Exception(f"file_id {file_id} not found")

        row_val = (row[0], row[1], row[2])
        return row_val

    except Exception as e:
        raise


def insert_state(conn, id: int, state: int) -> tuple:
    """
    0 = not started, 1 = migrated.
    """
    cursor = conn.cursor()
    try:
        upd = f'''
            UPDATE "{schema_name}"."file_bw_to_ds"
            SET "state" = ?
            WHERE "id" = ?
        '''
        cursor.execute(upd, [int(state), int(id)])
        conn.commit()
        
        # Fetch the row we just inserted
        sel = f'''
            SELECT "id", "state"
            FROM "{schema_name}"."file_bw_to_ds"
            WHERE "id" = ?
            ORDER BY "id" DESC
            LIMIT 1
        '''
        cursor.execute(sel, [int(id)])
        row = cursor.fetchone()
        print("👉", row)

        # Close connection
        cursor.close()
        if not row:
            raise Exception(f"Could not retrieve inserted state for file_id {id}")
        
        row_val = (row[0], row[1])
        return row_val

    except Exception as e:
        raise


def fetch_files(conn):
    cursor = conn.cursor()
    try:
        query = f'''
            SELECT 
                "id",
                "csv",
                "date",
                "csv_path",
                "json_path",
                "state"
            FROM "{schema_name}"."file_bw_to_ds"
            ORDER BY "id" DESC
        '''
        cursor.execute(query)
        rows = cursor.fetchall()
        print("👉", rows)

        # Close connection
        cursor.close()
        result = []
        for row in rows:
            result.append({
                "id": row[0],
                "csv": row[1],
                "date": row[2].isoformat() if row[2] else None,
                "csv_path": row[3],
                "json_path": row[4],
                "state": row[5]
            })

        return result

    except Exception as e:
        raise 
