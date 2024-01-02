from fastapi import APIRouter
router = APIRouter()

from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
# html 틀이 있는 폴더 위치
templates = Jinja2Templates(directory="templates/")

@router.get("/standard")
async def home(request:Request):
    pass
    return templates.TemplateResponse(name="homes/standard.html",context = {"request": request})
