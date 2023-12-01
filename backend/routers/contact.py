from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from backend.models.contact import FormData
from environment import variables
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

router = APIRouter(prefix="/contact", tags=["contact"])


@router.post("/submit-form", response_class=JSONResponse, status_code=status.HTTP_200_OK)
async def submit_form(form_data: FormData):

    html = f"""
    <!doctype html>
    <html lang="es">

    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #ffffff;
                color: #141414;
                margin: 0;
                padding: 0;
            }}

            .container {{
                width: 100%;
                max-width: 600px;
                margin: 0 auto;
                padding: 20px;
                box-sizing: border-box;
            }}

            .header {{
                text-align: center;
                padding-bottom: 20px;
            }}

            .header img {{
                max-width: 100%;
            }}

            .content {{
                padding: 20px;
                background-color: #eee8e8;
                border-radius: 10px;
                margin-top: 20px;
            }}
        </style>
    </head>

    <body>
        <div class="container">
            <div class="header">
                <img src="https://netflix.zeabur.app/logo.png" alt="Netflix Logo">
            </div>
            <div class="content">
                <h2>Formulario de Contacto</h2>
                <p>Nombre: {form_data.first_name} {form_data.last_name}</p>
                <p>Correo: {form_data.email}</p>
                <p>Mensaje: {form_data.message}</p>
            </div>
        </div>
    </body>

    </html>
    """

    try:
        message = MIMEMultipart()
        message["From"] = variables.sender_email
        message["To"] = ", ".join(
            [variables.david_email, variables.brandon_email])
        message["Subject"] = form_data.subject
        message.attach(MIMEText(html, "html"))

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(variables.sender_email, variables.sender_password)
        server.send_message(message)
        server.quit()

        return JSONResponse(content={"message": "Form submitted successfully"})
    except Exception as exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(exception))
