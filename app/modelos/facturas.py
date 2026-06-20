from pydantic import BaseModel, computed_field

from .transacciones import Transaccion
from .clientes import clientes 
from datetime import datetime

class FacturaBase(BaseModel):
    fecha: str = datetime.now()
    cliente: clientes
    transacciones: list[Transaccion] = []

    @computed_field
    @property
    def vr_total(self) -> float:

        factura_id_actual = getattr(self, "id", None)
        total_factura = 0.0
        if not factura_id_actual or not self.transacciones:
            return total_factura
        
        for transaccion in self.transacciones:
            if transaccion.factura_id == factura_id_actual:
                total_factura += transaccion.vr_unitario * transaccion.cantidad

        return total_factura

class FacturaCrear(FacturaBase):
    pass

class FacturaEditar(FacturaBase):
    pass

class Factura(FacturaBase):
    id: int | None = None