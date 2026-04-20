import os
from services.hana_service import get_db, get_state, get_file_paths_or_404, get_all_run_status
from services.file_service import json_file_name_generator, read_json_file, generate_json_file_path
from fastapi import APIRouter, Depends, UploadFile, File
from fastapi.responses import JSONResponse, FileResponse

router = APIRouter()

@router.get("/download_json/{file_id}")
def download_json_file(file_id: int, conn = Depends(get_db)):
    try:
        state = get_state(conn, file_id)
        file_name_with_csv = state["csv"]
        if state["state"] == 0:
            return JSONResponse(
                status_code=410,
                content={
                    "status": "error",
                    "status_code": 410,
                    "message": f"Conversion has not happened for file_id {file_id}.",
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

        csv_folder_path, json_folder_path = get_file_paths_or_404(conn, file_id)
        if not json_folder_path or not os.path.isdir(json_folder_path):
            return JSONResponse(
                status_code=404,
                content={
                    "status": "error",
                    "status_code": 404,
                    "message": f"Either json_folder_path not found in DB or json_folder_path is found in DB but not as a directory inside CF for file_id {file_id}",
                    "data": None,
                },
            )

        file_name_with_json = json_file_name_generator(file_name_with_csv)
        json_file_path = generate_json_file_path(json_folder_path, file_name_with_json)

        if not os.path.isfile(json_file_path):
            return JSONResponse(
                status_code=404,
                content={
                    "status": "error",
                    "status_code": 404,
                    "message": f"JSON file '{file_name_with_json}' not found.",
                    "data": None,
                },
            )

        return FileResponse(
            path=json_file_path,
            filename=file_name_with_json, 
            status_code= 200,
            media_type="application/json"
        )

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "status": "error",
                "status_code": 500,
                "message": f"Failed to download JSON: {str(e)}",
                "data": None
            }
        )