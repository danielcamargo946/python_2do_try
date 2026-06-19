from fastapi import FastAPI, HTTPException 
from modelos.clientes import clientes, clientecrear, ClienteEditar

app = FastAPI()

#modelo clientes (clase)

lista_clientes:list[clientes] = []

#endpoint para todos los clientes
@app.get("/clientes", response_model=list[clientes])
async def listar_clientes():
    return lista_clientes

#endpoint para un cliente
@app.get("/clientes{cliente_id}", response_model=clientes)
async def listar_cliente(cliente_id: int):
    #recorrer lista_clientes
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id  == cliente_id:
            return obj_cliente
 
#endpoint para crear un cliente en la lista
@app.post("/clientes", response_model=clientes)
async def crear_cliente(datos_cliente: clientecrear):
    cliente_val = clientes.model_validate(datos_cliente.model_dump())
    #agregar id 
    id_cliente = len(lista_clientes)+1
    cliente_val.id = id_cliente
    lista_clientes.append(cliente_val)
    return cliente_val


#endpoint para editar un cliente y agregar lista 
@app.patch("/clientes/{cliente_id}", response_model=clientes)
async def editar_cliente(cliente_id: int, datos_cliente: ClienteEditar):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id  == cliente_id:
            #validacion de cliente
            cliente_val = clientes.model_validate(datos_cliente.model_dump())
            cliente_val.id = cliente_id
            lista_clientes[i] = cliente_val
            return cliente_val
    raise HTTPException(
        status_code=400, detail=f"el cliente con id {cliente_id}, no existe")