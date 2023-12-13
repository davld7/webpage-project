from fastapi import FastAPI, HTTPException, status
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from backend.routers.contact import router as contact_router
from backend.database.client import client
from pymongo.errors import PyMongoError

app = FastAPI()

app.mount("/css", StaticFiles(directory="css"), name="css")
app.mount("/fonts", StaticFiles(directory="fonts"), name="fonts")
app.mount("/images", StaticFiles(directory="images"), name="images")
app.mount("/js", StaticFiles(directory="js"), name="js")
app.mount("/scss", StaticFiles(directory="scss"), name="scss")
app.include_router(contact_router)


@app.get("/", response_class=HTMLResponse, status_code=status.HTTP_200_OK)
async def index():
    path = "index.html"
    media_type = "text/html"
    return FileResponse(path=path, media_type=media_type)


@app.get("/favicon.ico", response_class=FileResponse, status_code=status.HTTP_200_OK)
async def favicon():
    path = "favicon.ico"
    media_type = "image/x-icon"
    return FileResponse(path=path, media_type=media_type)


@app.get("/logo.png", response_class=FileResponse, status_code=status.HTTP_200_OK)
async def logo():
    path = "logo.png"
    media_type = "image/png"
    return FileResponse(path=path, media_type=media_type)


@app.get("/ping", response_class=JSONResponse, status_code=status.HTTP_200_OK)
async def send_ping():
    try:
        client.admin.command('ping')
        message = "Pinged your deployment. You successfully connected to MongoDB!"
        return JSONResponse(content={"message": message})
    except PyMongoError as exception:
        detail = str(exception)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=detail)
