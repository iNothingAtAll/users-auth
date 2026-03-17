from api.models import TransaccionCreate, TransaccionResponse
from sqlmodel import Session
from fastapi import APIRouter, Depends, HTTPException
from api.database import get_session
from api.services.transacciones import TransaccionService

router = APIRouter()

def get_transaccion_service(session: Session = Depends(get_session)):
    return TransaccionService(session)

# Se define un endpoint para obtener información de una transacción específica por su ID
@router.get("/transaccion/{transaccion_id}", response_model=TransaccionResponse)
def obtener_transaccion(transaccion_id: int, transaccion_service: TransaccionService = Depends(get_transaccion_service)):
    transaccion = transaccion_service.get_transaccion(transaccion_id)
    if not transaccion:
        raise HTTPException(status_code=404, detail="Transacción no encontrada")
    return transaccion

# Se define un endpoint para crear una nueva transacción
@router.post("/transaccion/recargar", response_model=TransaccionResponse)
def recargar_saldo(data: TransaccionCreate, transaccion_service: TransaccionService = Depends(get_transaccion_service)):
    transaccion = transaccion_service.recargar(data)
    
    if not transaccion:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    return transaccion

# se define un endpoint para retirar saldo
@router.post("/transaccion/retirar", response_model=TransaccionResponse)
def retirar_saldo(data:TransaccionCreate, transaccion_service: TransaccionService = Depends(get_transaccion_service)):
    transaccion = transaccion_service.retirar(data)
    if not transaccion:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return transaccion


# Se define un endpoint para consultar saldo
@router.get("/usuario/{usuario_id}/saldo")
def consultar_saldo(usuario_id: int, transaccion_service: TransaccionService = Depends(get_transaccion_service)):
    transaccion = transaccion_service.consultar_saldo(usuario_id)
    if not transaccion:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return transaccion