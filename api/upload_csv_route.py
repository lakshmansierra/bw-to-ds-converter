import os
from datetime import date
from services.hana_service import get_db
from services.file_service import csv_file_path, json_file_path, write_uploaded_file
from services.hana_service import insert_file_record, insert_initial_conversion_run_status
from fastapi import APIRouter, Depends, UploadFile, File
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/upload_csv")
async def upload_csv_file(file: UploadFile = File(...), conn = Depends(get_db)):
    try:
        if not file.filename.lower().endswith(".csv"):
            return JSONResponse(
                status_code=400,
                content={
                    "status": "error",
                    "status_code": 400,
                    "message": "Only .csv files are allowed",
                    "data": None
                }
            )

        content = await file.read()

        # get file name
        file_name_with_csv = file.filename
        if file_name_with_csv is None:
            return JSONResponse(
                status_code=400,
                content={
                    "status": "error",
                    "status_code": 400,
                    "message": "Uploaded file has no filename",
                    "data": None
                }
            )
        file_name = os.path.splitext(file_name_with_csv)[0]

        # fix date
        uploaded_date =date.today()

        # get csv_folder_path
        csv_folder_path = csv_file_path(file_name)

        # get json_folder_path
        json_folder_path = json_file_path(file_name)

        # save file
        write_uploaded_file(csv_folder_path, file, file_name_with_csv)

        # insert into file_bw_to_ds
        inserted_id = insert_file_record(
            conn,
            csv=file_name,
            date=uploaded_date,
            csv_path=csv_folder_path,
            json_path=json_folder_path,
            state=int(0)
        )

        # insert initial run statuses (0) for conversion
        crs_id = insert_initial_conversion_run_status(conn, inserted_id)

        return JSONResponse(
            status_code=200,
            content={
                "status": "success",
                "status_code": 200,
                "message": "CSV metadata saved successfully",
                "data": {
                    "id": inserted_id,
                    "csv": file_name,
                    "date": uploaded_date.isoformat(),
                    "csv_folder_path": csv_folder_path,
                    "json_folder_path": json_folder_path,
                    "conversion_run_status_id": crs_id,
                }
            }
        )

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "status": "error",
                "status_code": 500,
                "message": f"Failed to upload CSV: {str(e)}",
                "data": None
            }
        )
