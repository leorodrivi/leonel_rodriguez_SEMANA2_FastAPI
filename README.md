# Mi Proyecto de API con FastAPI

## Descripción

Este es mi proyecto personal para aprender a crear APIs con FastAPI. He pasado de una API muy básica a una más completa, con validación de datos.

## Cómo ejecutar el proyecto

Para que esto funcione, necesitas tener **Python** instalado.

1.  Primero, instala las librerías:

    "pip install fastapi pydantic uvicorn"

2.  Luego, puedes arrancar la API con este comando en tu terminal:

    "uvicorn main:app --reload"

    Si todo sale bien, deberías poder ver mi API en `http://127.0.0.1:8000`.

-----

## Endpoints Principales

Aquí están las rutas que he creado hasta ahora:

  - `GET /`: Mensaje de bienvenida.
  - `GET /info`: Información sobre la API.
  - `GET /my-profile`: Mi perfil personal.
  - `POST /products`: Para agregar un nuevo producto.
  - `GET /products`: Para ver todos los productos que he agregado.
  - `GET /products/{id}`: Para ver un producto específico por su ID.
  - `GET /search`: Para buscar productos usando filtros.

-----

## Lo que he aprendido

En estas semanas, he logrado:

  - Crear una API con FastAPI y sus rutas (endpoints) básicas.
  - Usar type hints para que mi código sea más claro.
  - Implementar Pydantic para validar los datos que entran a la API, lo cual es muy útil.
  - Manejar parámetros de ruta y de búsqueda.
  - Generar la documentación automática de la API.
