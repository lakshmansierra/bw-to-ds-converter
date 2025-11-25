import os
from services.hana_service import get_db
from fastapi import APIRouter, Depends, UploadFile, File
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/download_json")
def download_json_file(conn = Depends(get_db)):
    try:
        return JSONResponse(
            status_code=400,
            content={
                "status": "error",
                "status_code": 400,
                "message": "Only .csv files are allowed",
                "data": None
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