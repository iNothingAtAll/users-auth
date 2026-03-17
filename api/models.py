from datetime import datetime
from pydantic import BaseModel, ConfigDict
from typing import Optional


class UserResponse(BaseModel):
    id: int
    nombre: str
    nickname: str
    saldo: float
    
    model_config = ConfigDict(from_attributes=True)


class UserCreate(BaseModel):
    nombre: str
    nickname: str
    identificacion: str
    correo: str
    telefono: str
    password_hash: str


class UserUpdate(BaseModel):
    nickname: str | None = None
    telefono: str | None = None
    correo: str | None = None
    password_hash: str | None = None


class TransaccionCreate(BaseModel):
    id_usuario: int
    monto: float
    descripcion: Optional[str] = None


class TransaccionResponse(BaseModel):
    id: int
    id_usuario: int
    tipo: str
    monto: float
    fecha: datetime
    descripcion: Optional[str] = None
    
    model_config = ConfigDict(from_attributes=True)