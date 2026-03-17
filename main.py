from fastapi import FastAPI
from contextlib import asynccontextmanager

from api.database import init_db, close_db_connection
from api.routes import users, transacciones


# Se inicializa la base de datos antes de empezar a escuchar peticiones
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Inicializando base de datos...")
    init_db()
    
    print("Base de datos lista")
    yield
    
    close_db_connection()


api = FastAPI(
    title="Users Auth",
    version="1.0.0", 
    lifespan=lifespan
)


api.include_router(users.router)
api.include_router(transacciones.router)