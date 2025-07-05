# CRUD de productos con nombre, descripción, precio y stock.
# Filtrado por categoría o rango de precios.

from fastapi import APIRouter, HTTPException
from src.models.models_catalog import Products, ProductsCreate, ProductsUpdate
from fastapi.responses import JSONResponse
from typing import List

route = APIRouter(prefix="/product")

products = [
    {
        "id": 1,
        "name": "Lenovo ThinkPad Laptop",
        "description": "Business laptop with Intel i5 processor and 16GB of RAM",
        "price": 950.00,
        "stock": 12,
        "category": "Technology"
    },
    {
        "id": 2,
        "name": "Sport Shirt Nike",
        "description": "Polyester t-shirt ideal for training",
        "price": 25.50,
        "stock": 35,
        "category": "Clothes"
    },
    {
        "id": 3,
        "name": "Ergonomic chair",
        "description": "Office chair with adjustable lumbar support",
        "price": 150.75,
        "stock": 8,
        "category": "furniture"
    }
]

#-----------
# ROUTES 
#-----------

def handle_exception(e: Exception):
    if isinstance(e, HTTPException):
        raise e  # si ya es una excepción HTTP, simplemente relanzala
    return JSONResponse(
        status_code=500,
        content={"error": str(e)}
    )

#READ
@route.get('/', response_model=List[Products], tags=['Products'] )
def get_all_products():
    try:
        return products
    except Exception as e:
        return handle_exception(e)

#CREATE
@route.post('/', response_model= List[ProductsCreate], tags=['Products'] )
def create_product(product: ProductsCreate):
    try:
        products.append(product.model_dump())
        return products
    except Exception as e:
        return handle_exception(e)

# UPDATE 
@route.put('/{id}', response_model= Products, tags=['Products'])
def update_product(id: int, data: ProductsUpdate):
    try:
        for product in products:
            if product['id'] == id:
                product['name'] = data.name
                product['description'] = data.description
                product['price'] = data.price
                product['stock'] = data.stock
                product['category'] = data.category
                return product
        raise HTTPException(404, 'Product not found :(')
    except Exception as e:
            return handle_exception(e)

# DELETE
@route.delete('/', response_model= List[Products], tags=['Products'])
def delete_product(id:int):
    try:
        for product in products:
            if product['id'] == id:
                products.remove(product)
                return products
        raise HTTPException(404, 'Product not found')
    except Exception as e:
        handle_exception(e)


#--------------------
# Products flitrated
#--------------------

# GET BY CATEGORY
@route.get('/category/{category}', response_model= List[Products], tags=['Filtrate products'])
def filtrate_products_by_category(category: str):
    try:
        filtered = [product for product in products if product['category'] == category]
        if not filtered:
            raise HTTPException(404, 'Product not found')
        return filtered
    except Exception as e:
        return handle_exception(e)

#RANGE OF PRICES 
@route.get('/filtered-by-price', response_model=List[Products], tags=['Filtrate products'])
def filtrate_by_range_of_price(price1: float = 0.0 , price2: float = 99999.0):
    try:
        filtered2 = [product for product in products if price1 <= product['price'] <= price2]
        return filtered2
    except Exception as e:
        return handle_exception(e)

















