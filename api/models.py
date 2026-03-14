from pydantic import BaseModel, ConfigDict


class UserResponse(BaseModel):
    id: int
    nombre: str
    nombre_publico: str
    saldo: float
    
    model_config = ConfigDict(from_attributes=True)
