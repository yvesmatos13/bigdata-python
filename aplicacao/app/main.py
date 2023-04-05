from fastapi import FastAPI

from app.server.routers import formulario_router as lojas


app = FastAPI(docs_url="/swagger", title="Estacio", version="1.0.0")

app.include_router(lojas.router)