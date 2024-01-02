from fastapi import APIRouter
router = APIRouter()

from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
# html 틀이 있는 폴더 위치
templates_po = Jinja2Templates(directory="templates/")

@router.get("/forms")
async def home4(request:Request):
    pass
    return templates_po.TemplateResponse(name="positionings/forms.html",context = {"request": request})

@router.get("/grids")
async def home5(request:Request):
    pass
    return templates_po.TemplateResponse(name="positionings/grids.html",context = {"request": request})

@router.get("/standard")
async def home6(request:Request):
    pass
    return templates_po.TemplateResponse(name="positionings/standard.html",context = {"request": request})

@router.get("/tables")
async def home7(request:Request):
    pass
    return templates_po.TemplateResponse(name="positionings/tables.html",context = {"request": request})

