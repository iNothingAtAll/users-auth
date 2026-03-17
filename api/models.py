from pydantic import BaseModel, ConfigDict


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