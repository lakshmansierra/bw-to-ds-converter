import os
import asyncio
from datetime import datetime
from services.hana_service import get_db, get_state, get_all_run_status, get_file_paths_or_404, set_conversion_run_status, insert_conversion_status, insert_state
from fastapi import APIRouter, Depends, UploadFile, File
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/convert_csv/{file_id}")
async def convert_csv_file(file_id: int, conn = Depends(get_db)):
    try:
        state = get_state(conn, file_id)
        if not state["state"] == 0:
            return JSONResponse(
                status_code=410,
                content={
                    "status": "error",
                    "status_code": 410,
                    "message": f"Conversion has already happened for file_id {file_id}.",
                    "data": {
                        "file_id": int(file_id),
                        "state": state["state"]
                    },
                },
            )

        run_status = get_all_run_status(conn, file_id)
        if run_status["conversion_run_status"] == 1:
            return JSONResponse(
                status_code=423,
                content={
                    "status": "error",
                    "status_code": 423,
                    "message": f"Conversion is currently running for file_id {file_id}. Try again after it completes.",
                    "data": {
                        "file_id": int(file_id),
                        "conversion_run_status": run_status["conversion_run_status"]
                    },
                },
            )

        csv_file_path, json_file_path = get_file_paths_or_404(conn, file_id)
        if not csv_file_path or not os.path.isdir(csv_file_path):
            return JSONResponse(
                status_code=404,
                content={
                    "status": "error",
                    "status_code": 404,
                    "message": f"Either csv_file_path not found in DB or csv_file_path is found in DB but not as a directory inside CF for file_id {file_id}",
                    "data": None,
                },
            )
            
        set_conversion_run_status(conn, file_id, 1)
        start_ts = datetime.utcnow()

        result = await asyncio.to_thread(run_conversion, csv_file_path, json_file_path)

        set_conversion_run_status(conn, file_id, 2)
        end_ts = datetime.utcnow()

        converted_json = result.get("converted_json") or {}

        if not converted_json:
            inserted_log = insert_conversion_status(conn, file_id, start_ts, end_ts, status=0)
            inserted_state = insert_state(conn, file_id, 0)
            return JSONResponse(
                status_code=422,
                content={
                    "status": "error",
                    "status_code": 422,
                    "message": "Conversion produced no json content.",
                    "data": {
                        "file_id": int(file_id),
                        "history_id": inserted_log[0],
                        "start_time": inserted_log[1].isoformat(),
                        "end_time": inserted_log[2].isoformat(),
                        "json_file_path": json_file_path,
                        "converted_json": converted_json,
                        "inserted_state": inserted_state[1]
                    },
                },
            )

        inserted_log = insert_conversion_status(conn, file_id, start_ts, end_ts, status=1)
        inserted_state = insert_state(conn, file_id, 1)
        return JSONResponse(
            status_code=200,
            content={
                "status": "success",
                "status_code": 200,
                "message": "Conversion completed",
                "data": {
                    "file_id": int(file_id),
                    "history_id": inserted_log[0],
                    "start_time": inserted_log[1].isoformat(),
                    "end_time": inserted_log[2].isoformat(),
                    "json_file_path": json_file_path,
                    "converted_json": converted_json,
                    "inserted_state": inserted_state[1]
                },
            },
        )

    except Exception as e:
        set_conversion_run_status(conn, file_id, 2)
        inserted_state = insert_state(conn, file_id, 0)
        return JSONResponse(
            status_code=500,
            content={
                "status": "error",
                "status_code": 500,
                "message": f"{str(e)}",
                "data": None,
            },
        )