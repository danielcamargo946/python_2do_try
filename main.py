from fastapi import FastAPI
from modelos.clientes import clientes, clientecrear

app = FastAPI()

#modelo clientes (clase)

lista_clientes:list[clientes] = []

#endpoint para todos los clientes
@app.get("/clientes", response_model=list[clientes])
def listar_clientes():
    return lista_clientes

#endpoint para un cliente
@app.get("/clientes{cliente_id}", response_model=clientes)
def listar_cliente(cliente_id: int):
    #recorrer lista_clientes
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.get("id") == cliente_id:
            return obj_cliente
 
#endpoint para crear un cliente en la lista
@app.post("/clientes", response_model=clientes)
def crear_cliente(datos_cliente: clientecrear):
    cliente_val = clientes.model_validate(datos_cliente.model_dump())
    lista_clientes.append(cliente_val)
    return cliente_val

