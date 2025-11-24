import os
from fastapi import APIRouter, Depends
from services.hana_service import get_db
from models.schemas import APIResponse

router = APIRouter()

@router.get("/convert_csv", response_model=APIResponse)
def convert_csv_file(conn = Depends(get_db)):
    try:
        response = APIResponse(
            status="success",
            status_code=200,
            message=f"",
            data={}
        ) 
        
    except Exception as e: 
        response = APIResponse(
            status="error",
            status_code=500,
            message=f"couldn't list files: {str(e)}",
            data=None
        )

    finally:
        return response