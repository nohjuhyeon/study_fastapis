from fastapi import APIRouter
router = APIRouter()

from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
# html 틀이 있는 폴더 위치
templates = Jinja2Templates(directory="templates/")

# 회원 가입 from /users/form -> users/inserts.html
@router.post("/inserts")
async def home(request:Request):
    print(dict(await request.form()))
    pass
    return templates.TemplateResponse(name="users/inserts.html",context = {"request": request})

@router.get("/inserts")
async def home(request:Request):
    print(dict(request.query_params))
    pass
    return templates.TemplateResponse(name="users/inserts.html",context = {"request": request})


# 회원 가입 /users/inserts -> users/login.html
@router.post("/logins")
async def home(request:Request):
    print(dict(await request.form()))
    pass
    return templates.TemplateResponse(name="users/logins.html",context = {"request": request})

# 회원 리스트 /users/lists -> users/lists.html
@router.post("/lists")
async def home(request:Request):
    print(dict(await request.form()))
    pass
    return templates.TemplateResponse(name="users/lists.html",context = {"request": request})

@router.get("/lists")
async def home(request:Request):
    print(dict(request.query_params))
    pass
    return templates.TemplateResponse(name="users/lists.html",context = {"request": request})

# 회원 리스트 /users/reads -> users/reads.html
# Path parameters : /users/reads/id or /users/read/unique_name
@router.get("/reads/{object_id}")
async def home(request:Request, object_id):
    print(object_id)
    pass
    return templates.TemplateResponse(name="users/reads.html",context = {"request": request})

@router.get("/reads/{object_id}")
async def home(request:Request, object_id):
    print(object_id)
    pass
    return templates.TemplateResponse(name="users/reads.html",context = {"request": request})
