# 🛒 FastAPI Catalog

Proyecto simple de API REST creada con FastAPI para gestionar un catálogo de productos.

## 🚀 Tecnologías usadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic](https://docs.pydantic.dev/)
- [Uvicorn](https://www.uvicorn.org/) (para correr el servidor)

## 📁 Estructura del proyecto

FastAPI Catalog/
├── main.py
└── src/
├── routes/
│ └── routes_catalog.py
└── models/
└── models_catalog.py


## 📦 Instalación

1. Clona este repositorio:
    ```bash
    git clone https://github.com/tu-usuario/FastAPI-Catalog.git
    cd FastAPI-Catalog

2. Crea un entorno virtual:

    python -m venv .venv
    source .venv/bin/activate  # En Windows: .venv\Scripts\activate

3. Instala las dependencias:

    pip install -r requirements.txt

▶️ Ejecución del servidor:

    uvicorn main:app --reload

Accede a la documentación interactiva en:

Swagger UI: http://localhost:8000/docs

Redoc: http://localhost:8000/redoc

📌 Estado
✅ Proyecto en fase funcional inicial.
🛠️ Puedes extenderlo agregando conexión con base de datos, autenticación, validaciones, etc.

¡Gracias por visitar este repositorio!