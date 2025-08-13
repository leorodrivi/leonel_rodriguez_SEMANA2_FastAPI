from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List, Dict, Any

app = FastAPI(title="Mi API Fusionada")

class Product(BaseModel):
    name: str
    price: int
    available: bool = True

class ProductResponse(BaseModel):
    id: int
    name: str
    price: int
    available: bool
    message: str = "Operación exitosa"

class ProductListResponse(BaseModel):
    products: List[dict]
    total: int
    message: str = "Lista recuperada"

class CompleteUser(BaseModel):
    name: str
    age: int
    email: str
    phone: Optional[str] = None
    active: bool = True

products = []

@app.get("/")
def home() -> dict:
    return {"message": "¡Hola! Bienvenido a mi API fusionada"}

@app.get("/info")
def get_info() -> dict:
    return {
        "api_name": "Mi API Fusionada",
        "version": "1.0",
        "author": "Leonel Rodriguez"
    }

@app.get("/my-profile")
def my_profile() -> dict:
    return {
        "name": "Leonel Rodriguez",
        "bootcamp": "FastAPI",
        "week": "Semana 1 y 2",
        "date": "2025",
        "likes_fastapi": True
    }

@app.post("/users", status_code=201)
def create_user(user: CompleteUser) -> dict:
    return {"user": user.dict(), "valid": True, "message": "Usuario creado"}

@app.get("/products", response_model=ProductListResponse)
def get_products() -> ProductListResponse:
    return ProductListResponse(products=products, total=len(products))

@app.post("/products", response_model=ProductResponse, status_code=201)
def create_product(product: Product) -> ProductResponse:
    product_dict = product.dict()
    product_dict["id"] = len(products) + 1
    products.append(product_dict)
    return ProductResponse(**product_dict, message="Producto creado exitosamente")

@app.get("/products/{product_id}")
def get_product(product_id: int) -> dict:
    for product in products:
        if product["id"] == product_id:
            return {"product": product}
    raise HTTPException(status_code=404, detail="Producto no encontrado")

@app.get("/search")
def search_products(
    name: Optional[str] = None,
    max_price: Optional[int] = None,
    available: Optional[bool] = None
) -> dict:
    results = products.copy()
    if name:
        results = [p for p in results if name.lower() in p["name"].lower()]
    if max_price:
        results = [p for p in results if p["price"] <= max_price]
    if available is not None:
        results = [p for p in results if p["available"] == available]
    return {"results": results, "total": len(results)}

@app.get("/categories/{category}/products/{product_id}")
def product_by_category(category: str, product_id: int) -> dict:
    return {
        "category": category,
        "product_id": product_id,
        "message": f"Buscando el producto {product_id} en la categoría {category}"
    }