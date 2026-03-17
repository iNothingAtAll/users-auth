from fastapi import HTTPException
from sqlmodel import Session
from api.schemas import Transaccion, Usuario
from api.models import TransaccionCreate
from sqlmodel import Session, select

class TransaccionService:
    def __init__(self, session: Session):
        self.session = session

    def recargar(self, data: TransaccionCreate):
        usuario = self.session.get(Usuario, data.id_usuario)
        usuario.saldo += data.monto
        self.session.add(usuario)
        self.session.commit()
        return self.crear_transaccion(data)
        
    def retirar(self, data: TransaccionCreate):
        usuario = self.session.get(Usuario, data.id_usuario)
        if usuario.saldo < data.monto:
            raise HTTPException(status_code=400, detail="Saldo insuficiente")
        usuario.saldo -= data.monto
        self.session.add(usuario)
        self.session.commit()
        return self.crear_transaccion(data)


    def crear_transaccion(self, data: TransaccionCreate):
        nueva_transaccion = Transaccion(**data.model_dump())
        self.session.add(nueva_transaccion)
        self.session.commit()
        self.session.refresh(nueva_transaccion)
        return nueva_transaccion


    def consultar_saldo(self, id_usuario: int):
        usuario = self.session.get(Usuario, id_usuario)
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return {"saldo": usuario.saldo}
    
    def get_transacciones(self, id_usuario: int):
        transacciones = self.session.exec(select(Transaccion).where(Transaccion.id_usuario == id_usuario)).all()
        return transacciones