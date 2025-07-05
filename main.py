from fastapi import FastAPI
from src.routes.routes_catalog import route

app = FastAPI(title='Catalog Products')
app.include_router(router=route)