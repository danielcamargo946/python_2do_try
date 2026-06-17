from pydantic import BaseModel

class clienteBase(BaseModel):
    nombre: str
    email: str
    descripcion: str


class clientecrear(clienteBase):
    pass


class clientes(clienteBase):
    id: int | None = None