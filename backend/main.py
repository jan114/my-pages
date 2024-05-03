from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()
app.mount("/scripts", StaticFiles(directory="frontend/static/scripts"), "scripts")
app.mount("/styles", StaticFiles(directory="frontend/static/styles"), "styles")
templates = Jinja2Templates("frontend/templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(request, "index.html")