from pydantic import BaseModel, ConfigDict


class UserResponse(BaseModel):
    id: int
    nombre: str
    nombre_publico: str
    saldo: float
    
    model_config = ConfigDict(from_attributes=True)


class UserCreate(BaseModel):
    nombre: str
    nombre_publico: str
    telefono: str
    correo: str
    password_hash: str


class UserUpdate(BaseModel):
    nombre_publico: str | None = None
    telefono: str | None = None
    correo: str | None = None
    password_hash: str | None = None