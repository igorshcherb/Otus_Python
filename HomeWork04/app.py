from fastapi import FastAPI, Request
from routers.item_routers import router as item_router
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory='templates')


# /
@app.get("/")
async def show_index(request: Request):
    context = {
        'request': request,
    }
    return templates.TemplateResponse('index.html', context=context)


# /about/
@app.get("/about/")
async def show_about(request: Request):
    context = {
        'request': request,
    }
    return templates.TemplateResponse('about.html', context=context)


app.include_router(item_router, prefix='/api', tags=['item_routers'])
