from fastapi import FastAPI
from contextlib import asynccontextmanager

from api.database import init_db, close_db_connection


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


# Muestra todos los enpoint de la api en los que se puede acceder de forma publica
@api.get("/info", tags=["info"])
async def get_info():
    return {
        "title": api.title,
        "version": api.version,
        "routes": {
            "info" : {"endpoint":"http://localhost:8000/info", "method":"GET"},
        }
    }