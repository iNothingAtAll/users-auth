from fastapi import HTTPException
from sqlmodel import Session
from api.schemas import RecargaInput, RetirarInput, Transaccion, Usuario

class TransaccionService:
    def __init__(self, session: Session):
        self.session = session

    def recargar(self, data: RecargaInput):
        usuario = self.session.get(Usuario, data.id_usuario)
        usuario.saldo += data.monto
        self.session.add(usuario)
        self.session.commit()
        nueva_transaccion = Transaccion(**data.model_dump())
        self.session.add(nueva_transaccion)
        self.session.commit()
        self.session.refresh(nueva_transaccion)
        return nueva_transaccion
        
    def retirar(self, data: RetirarInput):
        usuario = self.session.get(Usuario, data.id_usuario)
        if usuario.saldo < data.monto:
            raise HTTPException(status_code=400, detail="Saldo insuficiente")
        usuario.saldo -= data.monto
        self.session.add(usuario)
        self.session.commit()
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