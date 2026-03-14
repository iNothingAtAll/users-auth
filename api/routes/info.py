from sqlmodel import Session
from fastapi import APIRouter, Depends, HTTPException

from api.database import get_session
from api.schemas import Usuario
from api.models import UserResponse


router = APIRouter(prefix="/info", tags=["info"])


# Se define un endpoint para obtener información de un usuario específico por su ID
@router.get("/usuario/{usuario_id}", response_model=UserResponse)
def obtener_usuario(usuario_id: int, session: Session = Depends(get_session)):
    usuario = session.get(Usuario, usuario_id)
   
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    return usuario