import os
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from services.hana_service import get_db

router = APIRouter()

@router.get("/list_json")
def list_json_file(conn = Depends(get_db)):
    try:
        return JSONResponse(
            status_code=200,
            content={
                "status": "success",
                "status_code": 200,
                "message": f"",
                "data": {},
            },
        )

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "status": "error",
                "status_code": 500,
                "message": f"couldn't list files: {str(e)}",
                "data": None,
            },
        )
