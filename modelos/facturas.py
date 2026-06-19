from pydantic import BaseModel
from .clientes import clientes 

class FacturaBase(BaseModel):
    fecha: str
    vr_total: float 
    cliente: clientes

class FacturaCrear(FacturaBase):
    pass

class Factura(FacturaBase):
    id: int | None = None