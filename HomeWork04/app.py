from fastapi import FastAPI
from routers.item_routers import router as item_router

app = FastAPI()


# /
@app.get("/")
async def root():
    return {"message": "Hello World"}


# /about/
@app.get("/about/")
async def root():
    return {"message": "Первое веб-приложение"}


app.include_router(item_router, prefix='/api', tags=['item_routers'])
