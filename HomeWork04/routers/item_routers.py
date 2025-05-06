from fastapi import APIRouter, Request
from pydantic import BaseModel, Field
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory='templates')


class FoodUpdate(BaseModel):
    name: str = Field(..., title='Food Name', max_length=20)
    weight: float = Field(None, title='Food weight', ge=0, le=100_000)
    price: float = Field(None, title='Food price', ge=0, le=100_000)
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
async def list_foods(request: Request):
    context = {
        'request': request,
        'title': 'Список продуктов',
        'foods': foods,
    }
    return templates.TemplateResponse('list.html', context=context)


@router.get("/food/{food_pk}")
async def read_food(food_pk: int, request: Request):
    food = None
    for food in foods:
        if food.pk == food_pk:
            break
    context = {
        'request': request,
        'title': 'Пищевой продукт',
        'food': food,
    }
    return templates.TemplateResponse('food.html', context=context)


@router.post("/add/")
async def add_food(food: Food):
    foods.append(food)
    return {"food": food}


@router.put("/update/{food_pk}")
async def update_food(food_pk: int, upd_food: FoodUpdate):
    for food in foods:
        if food.pk == food_pk:
            food.name = upd_food.name
            food.price = upd_food.price
            food.weight = upd_food.weight
            food.description = upd_food.description
            return {'Message': f'Продукт {food} обновлен'}
    return {"Message": 'Продукт не найден'}


@router.delete("/delete/{food_pk}")
async def delete_product(food_pk: int):
    for food in foods:
        if food.pk == food_pk:
            foods.remove(food)
            return {'Message': f'Продукт {food} удален'}
    return {"Message": 'Продукт не найден'}
