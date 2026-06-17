from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#modelo clientes (clase)

class clientes(BaseModel):
    id: int
    nombre: str
    email: str
    descripcion: str

lista_clientes:list[clientes] = []

#endpoint para todos los clientes
@app.get("/clientes")
def listar_clientes():
    return lista_clientes

#endpoint para un cliente
@app.get("/clientes{cliente_id}")
def listar_cliente(cliente_id: int):
    #recorrer lista_clientes
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.get("id") == cliente_id:
            return obj_cliente
 
#endpoint para crear un cliente en la lista
@app.post("/clientes")
def crear_cliente(datos_cliente: clientes):
    lista_clientes.append(datos_cliente)
    return datos_cliente