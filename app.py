from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/greet", response_class=HTMLResponse)
async def greet(request: Request, name: str = Form(...), age: int = Form(...)):
    if not name or age < 0:
        error = "Please enter a valid name and age."
        return templates.TemplateResponse("index.html", {"request": request, "error": error})

    age_msg = "You're just getting started!" if age < 30 else "Wisdom suits you well."
    return templates.TemplateResponse("greet.html", {
        "request": request,
        "name": name,
        "age": age,
        "age_msg": age_msg
    })

@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

@app.exception_handler(404)
async def not_found(request: Request, exc):
    return templates.TemplateResponse("404.html", {"request": request}, status_code=404)