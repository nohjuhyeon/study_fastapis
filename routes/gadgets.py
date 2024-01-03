from fastapi import APIRouter
router = APIRouter()

from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
# html 틀이 있는 폴더 위치
templates = Jinja2Templates(directory="templates/")

@router.get("/buttons")
async def home(request:Request):
    pass
    return templates.TemplateResponse(name="gadgets/buttons.html",context = {"request": request})
@router.get("/cards")
async def home1(request:Request):
    pass
    return templates.TemplateResponse(name="gadgets/cards.html",context = {"request": request})
@router.get("/colors")
async def home2(request:Request):
    pass
    return templates.TemplateResponse(name="gadgets/colors.html",context = {"request": request})
@router.get("/containers")
async def home3(request:Request):
    pass
    return templates.TemplateResponse(name="gadgets/containers.html",context = {"request": request})


 