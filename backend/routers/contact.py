from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from backend.models.contact import FormData
from environment import variables

router = APIRouter(prefix="/contact", tags=["contact"])


@router.post("/submit-form", response_class=JSONResponse, status_code=status.HTTP_200_OK)
async def submit_form(form_data: FormData):
    print(form_data.first_name)
    print(form_data.last_name)
    print(form_data.email)
    print(form_data.subject)
    print(form_data.message)
    print(variables.sender_email)
    print(variables.sender_password)
    return JSONResponse(content={"message": "Form submitted successfully"})
