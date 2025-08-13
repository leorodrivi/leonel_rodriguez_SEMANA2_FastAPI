from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI(title="Mi API de Productos")

products = [
    {"id": 1, "name": "Laptop", "price": 1200, "available": True},
    {"id": 2, "name": "Mouse", "price": 25, "available": True},
    {"id": 3, "name": "Teclado", "price": 75, "available": False},
]

class Product(BaseModel):
    name: str
    price: int
    available: bool = True

@app.get("/")
def home() -> dict:
    return {"message": "¡Bienvenido a la API de productos!"}

@app.get("/products")
def get_products() -> List[dict]:
    return products

@app.get("/products/{product_id}")
def get_product(product_id: int) -> dict:
    for product in products:
        if product["id"] == product_id:
            return product
    raise HTTPException(status_code=404, detail="Producto no encontrado")

@app.post("/products", status_code=201)
def create_product(product: Product) -> dict:
    product_dict = product.dict()
    new_id = max(p["id"] for p in products) + 1 if products else 1
    product_dict["id"] = new_id
    products.append(product_dict)
    return product_dict

@app.get("/search")
def search_products(
    name: Optional[str] = None,
    max_price: Optional[int] = None
) -> List[dict]:
    results = products.copy()
    if name:
        results = [p for p in results if name.lower() in p["name"].lower()]
    if max_price:
        results = [p for p in results if p["price"] <= max_price]
    return results
