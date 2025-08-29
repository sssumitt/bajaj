# app/router.py

from fastapi import APIRouter, HTTPException
from . import schemas, services, config

router = APIRouter()

@router.post("/bfhl", response_model=schemas.ResponseData)
async def process_data_endpoint(payload: schemas.RequestData):
  
    try:
        processed_data = services.process_array_data(payload.data)
        
        user_id = f"{config.FULL_NAME.lower().replace(' ', '_')}_{config.DOB}"

        return {
            "is_success": True,
            "user_id": user_id,
            "email": config.EMAIL,
            "roll_number": config.ROLL_NUMBER,
            **processed_data 
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail={"is_success": False, "error": str(e)})