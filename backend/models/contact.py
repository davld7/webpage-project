from pydantic import BaseModel


class FormData(BaseModel):
    first_name: str
    last_name: str
    email: str
    subject: str
    message: str
