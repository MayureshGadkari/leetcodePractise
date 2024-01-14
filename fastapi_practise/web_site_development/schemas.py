from pydantic import BaseModel

class get_details_request(BaseModel):
    user_id: int

class create_user(BaseModel):
    user_name: str
    phone_number: int
    gender: str
    email_id: str
    category: str
    model: str
    plate_no:str
