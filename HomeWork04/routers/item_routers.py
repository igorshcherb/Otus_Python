from fastapi import APIRouter, Request
from pydantic import BaseModel, Field
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory='templates')


class FoodUpdate(BaseModel):
    name: str = Field(..., title='Food Name', max_length=20)
    weight: float = Field(..., title='Food weight', ge=0, le=100_000)
    price: float = Field(..., title='Food price', ge=0, le=100_000)
    description: str = Field(None, title='Description', max_length=1000)


class Food(FoodUpdate):
    pk: int


foods = [
    Food(
        pk=1,
        name='хлеб',
        weight=500.0,
        price=50.0,
        description='Хлеб в упаковке'
    ),
    Food(
        pk=2,
        name='масло',
        weight=200.0,
        price=250.0,
        description='Масло в пачке'
    ),
    Food(
        pk=3,
        name='молоко',
        weight=1000.0,
        price=90.0,
        description='Молоко в бутылке'
    )
]


# /list/
@router.get("/list/")
async def read_foods(request: Request):
    context = {
        'request': request,
        'title': 'Список продуктов',
        'foods': foods,
    }
    return templates.TemplateResponse('list.html', context=context)
