from pydantic import BaseModel, Field

class Products(BaseModel):
    id: int
    name:str
    description: str
    price: float
    stock: int
    category: str

class ProductsCreate(BaseModel):
    id: int
    name:str = Field(..., min_length=3, max_length=35)
    description: str = Field(..., min_length=5, max_length=80)
    price: float = Field(..., ge=1)
    stock: int
    category: str = Field(..., min_length=3)

    model_config = {
        'json_schema_extra': {
            'example': {
                'id': 1,
                'name':'Nerf gun',
                'description': 'Nerf gun for kids, with long-lasting battery.',
                'price': 15.5,
                'stock': 12,
                'category': 'Toys weapons'
            }
        }
    }

class ProductsUpdate(BaseModel):
    name: str
    description: str
    price: float
    stock: int
    category: str