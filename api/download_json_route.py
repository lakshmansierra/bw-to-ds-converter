import os
from services.hana_service import get_db, get_state, get_file_paths_or_404
from services.file_service import json_file_generator
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

        csv_file_path, json_file_path = get_file_paths_or_404(conn, file_id)
        if not json_file_path or not os.path.isdir(json_file_path):
            return JSONResponse(
                status_code=404,
                content={
                    "status": "error",
                    "status_code": 404,
                    "message": f"Either json_file_path not found in DB or json_file_path is found in DB but not as a directory inside CF for file_id {file_id}",
                    "data": None,
                },
            )

        json_filename, json_file_full_path = json_file_generator(file_name_with_csv=file_name_with_csv, json_file_path=json_file_path)

        if not os.path.isfile(json_file_full_path):
            return JSONResponse(
                status_code=404,
                content={
                    "status": "error",
                    "status_code": 404,
                    "message": f"JSON file '{json_filename}' not found.",
                    "data": None,
                },
            )

        return FileResponse(
            path=json_file_full_path,
            filename=json_filename, 
            status_code= 200,
            media_type="application/json"
        )

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "status": "error",
                "status_code": 500,
                "message": f"Failed to download json: {str(e)}",
                "data": None
            }
        )