from fastapi import APIRouter
from httpx import QueryParams
router = APIRouter()

from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
# html 틀이 있는 폴더 위치
templates = Jinja2Templates(directory="templates/")

@router.get("/buttons")
async def home(request:Request):
    return templates.TemplateResponse(name="gadgets/buttons.html",context = {"request": request})
@router.post("/cards")
# request = Request(query_parameters)
async def home1(request:Request):
    # request.query_params
    # QueryParams('')
    # await request.form()
    # FormData([('name', 'gocolab'), ('email', 'info@gocolab.com')])
    # dict(await request.form())
    # {'name': 'gocolab', 'email': 'info@gocolab.com'}
    # form_datas = await request.form()
    # dict(form_datas)
    return templates.TemplateResponse(name="gadgets/cards.html",context = {"request": request})
@router.get("/cards")
    # request.query_params
    # QueryParams('name=gocolab&email=info%40gocolab.com')
    # dict(request.query_params)
    # {'name': 'gocolab', 'eremail': 'info@gocolab.com'}
async def home1(request:Request):

    return templates.TemplateResponse(name="gadgets/cards.html",context = {"request": request})
@router.get("/colors")
async def home2(request:Request):
    # form_datas = await request.form()
    return templates.TemplateResponse(name="gadgets/colors.html",context = {"request": request})
@router.get("/containers")
async def home3(request:Request):
    return templates.TemplateResponse(name="gadgets/containers.html",context = {"request": request})


 