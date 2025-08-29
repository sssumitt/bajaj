# app/schemas.py

from pydantic import BaseModel, EmailStr
from typing import List, Any


class RequestData(BaseModel):
    data: List[Any]

class ResponseData(BaseModel):
    is_success: bool
    user_id: str
    email: EmailStr
    roll_number: str
    odd_numbers: List[str]
    even_numbers: List[str]
    alphabets: List[str]
    special_characters: List[str]
    sum: str
    concat_string: str