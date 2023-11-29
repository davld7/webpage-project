from fastapi import APIRouter, HTTPException, status
from fastapi.responses import FileResponse, JSONResponse
from backend.models.contact import FormData
from environment import variables
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

router = APIRouter(prefix="/contact", tags=["contact"])


@router.get("/style.css", response_class=FileResponse, status_code=status.HTTP_200_OK)
async def contact_style():
    path = "css/contact.css"
    mediatype = "text/css"
    return FileResponse(path=path, media_type=mediatype)


@router.post("/submit-form", response_class=JSONResponse, status_code=status.HTTP_200_OK)
async def submit_form(form_data: FormData):

    html = f"""
    <!doctype html>
    <html lang="es">

    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="https://netflix.zeabur.app/contact/style.css">
        <title>Correo Electrónico</title>
    </head>

    <body>
        <div class="container">
            <div class="header">
                <img src="https://netflix.zeabur.app/logo.png" alt="Netflix Logo">
            </div>
            <div class="content">
                <h2>¡Nuevo Formulario de Contacto!</h2>
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
        message["To"] = "davld7@outlook.com"
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
