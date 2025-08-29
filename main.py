from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Any

app = FastAPI()

class RequestData(BaseModel):
    data: List[Any]

@app.get("/")
def read_root():
    return {"message": "Server is running", "operation_code": 1}

@app.post("/bfhl")
async def process_data(payload: RequestData):
    try:
        full_name = "Sumit Anand"
        dob = "19072003"  # DDMMYYYY
        email_id = "sumit.2022@vitstudent.ac.in"
        roll_number = "22BCE3374"
        user_id = f"{full_name.lower().replace(' ', '_')}_{dob}"

        data = payload.data

        odd_numbers = []
        even_numbers = []
        alphabets = []
        special_characters = []
        all_alphabetic_chars = []
        total_sum = 0

        for item in data:
            item_str = str(item)
            if item_str.isalpha():
                alphabets.append(item_str.upper())
                all_alphabetic_chars.extend(list(item_str))
            elif item_str.isdigit():
                num = int(item_str)
                total_sum += num
                (even_numbers if num % 2 == 0 else odd_numbers).append(item_str)
            else:
                special_characters.append(item_str)

        all_alphabetic_chars.reverse()
        concat_string = "".join(
            c.upper() if i % 2 == 0 else c.lower()
            for i, c in enumerate(all_alphabetic_chars)
        )

        return {
            "is_success": True,
            "user_id": user_id,
            "email": email_id,
            "roll_number": roll_number,
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_characters,
            "sum": str(total_sum),
            "concat_string": concat_string
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail={"is_success": False, "error": str(e)})
