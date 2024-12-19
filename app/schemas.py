from pydantic import BaseModel
from datetime import datetime

class CanchaBase(BaseModel):
    nombre: str
    techada: bool

class CanchaCreate(CanchaBase):
    pass

class Cancha(CanchaBase):
    id: int
    class Config:
        from_attributes = True

class ReservaBase(BaseModel):
    dia: datetime
    duracion: int
    contacto_nombre: str
    contacto_telefono: str

class ReservaCreate(ReservaBase):
    cancha_id: int

class Reserva(ReservaBase):
    id: int
    cancha: Cancha
    class Config:
        from_attributes = True
