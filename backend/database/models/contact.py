from pydantic import BaseModel
from typing import Optional


class FormData(BaseModel):
    first_name: str
    last_name: str
    email: str
    subject: str
    message: str


class FormDataWithId(BaseModel):
    id: Optional[str]
    first_name: str
    last_name: str
    email: str
    subject: str
    message: str
