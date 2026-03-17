from sqlmodel import SQLModel, Field, Relationship, Column, Boolean
from typing import Optional, List
from datetime import datetime


# Modelo de Usuario
class Usuario(SQLModel, table=True):
    __tablename__ = "usuarios"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(unique=True, index=True, max_length=255)
    nickname: str = Field(max_length=255)
    identificacion: str = Field(unique=True, index=True, max_length=255)
    correo: str = Field(unique=True, index=True, max_length=255)
    telefono: Optional[str] = Field(default=None, max_length=20)
    password_hash: str = Field(max_length=255)
    saldo: float = Field(default=0.0)
    fecha_registro: datetime = Field(default_factory=datetime.now)
    activo: bool = Field(default=True, sa_column=Column(Boolean))
    
    # Relaciones
    transacciones: List["Transaccion"] = Relationship(back_populates="usuario")


# Modelo de Transacción
class Transaccion(SQLModel, table=True):
    __tablename__ = "transacciones"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    id_usuario: int = Field(foreign_key="usuarios.id")
    tipo: str = Field(max_length=20)
    monto: float
    fecha: datetime = Field(default_factory=datetime.now)
    descripcion: Optional[str] = Field(default=None, max_length=255)
    
    # Relación
    usuario: Usuario = Relationship(back_populates="transacciones")
