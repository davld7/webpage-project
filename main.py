from fastapi import FastAPI, Request, status
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/css", StaticFiles(directory="css"), name="css")
app.mount("/fonts", StaticFiles(directory="fonts"), name="fonts")
app.mount("/images", StaticFiles(directory="images"), name="images")
app.mount("/js", StaticFiles(directory="js"), name="js")
app.mount("/scss", StaticFiles(directory="scss"), name="scss")


@app.middleware("http")
async def redirect_middleware(request: Request, call_next):
    if request.url.path == "/index.html":
        return RedirectResponse(url="/")
    return await call_next(request)


@app.get("/", response_class=HTMLResponse, status_code=status.HTTP_200_OK)
async def index():
    path = "index.html"
    media_type = "text/html"
    return FileResponse(path=path, media_type=media_type)


@app.get("/favicon.png", response_class=FileResponse, status_code=status.HTTP_200_OK)
async def favicon():
    path = "favicon.png"
    media_type = "image/png"
    return FileResponse(path=path, media_type=media_type)
