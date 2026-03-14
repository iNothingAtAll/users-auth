from sqlmodel import Session
from fastapi import APIRouter, Depends, HTTPException

from api.database import get_session
from api.models import UserResponse, UserCreate, UserUpdate
from api.services.users import UserService


router = APIRouter()


def get_user_service(session: Session = Depends(get_session)):
    return UserService(session)


# Se define un endpoint para obtener información de un usuario específico por su ID
@router.get("/usuario/{usuario_id}", response_model=UserResponse)
def obtener_usuario(usuario_id: int, user_service: UserService = Depends(get_user_service)):
    usuario = user_service.get_user(usuario_id)
   
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    return usuario


# Se define un endpoint para actualizar información de un usuario específico por su ID
@router.put("/usuario/{usuario_id}", response_model=UserResponse)
def actualizar_usuario(usuario_id: int, user_data: UserUpdate, user_service: UserService = Depends(get_user_service)):
    usuario = user_service.update_user(usuario_id, user_data)
   
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    return usuario


# Se define un endpoint para deshabilitar un usuario específico por su ID
@router.put("/usuario/{usuario_id}/deshabilitar", response_model=UserResponse)
def disable_user(usuario_id: int, user_service: UserService = Depends(get_user_service)):
    usuario = user_service.disable_user(usuario_id)
   
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    return usuario


# Se define un endpoint para crear un nuevo usuario
@router.post("/usuario", response_model=UserResponse)
def crear_usuario(user_data: UserCreate, user_service: UserService = Depends(get_user_service)):
    usuario = user_service.create_user(user_data)
    return usuario