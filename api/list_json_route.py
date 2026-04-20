import os
from services.hana_service import get_db, fetch_files, get_all_run_status
from fastapi import APIRouter, Depends, UploadFile, File
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/list_json")
def list_json_file(conn = Depends(get_db)):
    try:
        rows = fetch_files(conn)
        return JSONResponse(
            status_code=200,
            content={
                "status": "success",
                "status_code": 200,
                "message": f"fetched {len(rows)}",
                "data": rows,
            },
        )

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "status": "error",
                "status_code": 500,
                "message": f"couldn't fetch files: {str(e)}",
                "data": None,
            },
        )