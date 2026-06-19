from fastapi import FastAPI, HTTPException, status
from modelos.clientes import clientes, clientecrear, ClienteEditar
from modelos.facturas import Factura, FacturaCrear, FacturaEditar
from modelos.transacciones import Transaccion, TransaccionCrear, TransaccionEditar

app = FastAPI()

#modelo clientes (clase)

lista_clientes:list[clientes] = []
lista_facturas: list[Factura] = []
#lista_transacciones: list[transacciones] = []

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
    raise HTTPException(tatus_code=400, detail=f"el cliente con id {cliente_id}, no existe")
 
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

#endpoint para eliminar un cliente 
@app.delete("/clientes/{cliente_id}", response_model=clientes)
async def eliminar_cliente(cliente_id: int):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id  == cliente_id:
            cliente_eliminado = lista_clientes.pop(i)
            return cliente_eliminado
    raise HTTPException(
        status_code=400, detail=f"el cliente con id {cliente_id}, no existe")


#=========================================================================================================================
#endpoint para facturas

@app.get("/facturas", response_model=list[Factura])
async def listar_facturas():
    return lista_facturas  

@app.get("/facturas/{id_factura}", response_model=list[Factura])
async def listar_facturas(id_factura: int):
     #recorrer lista_facturas
    for i, obj_Factura in enumerate(lista_facturas):
        if obj_Factura.id  == id_factura:
            return obj_Factura
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"la factura con id {id_factura}, no existe")

@app.post("/facturas/{clinte_id}", response_model=Factura)
async def crear_facturas(id_factura: int, datos_factura: Factura):
    #buscar el cliente
    cliente_encontrado = None
    for cliente in lista_clientes:
        if cliente.id == cliente_id:
            cliente_encontrado = cliente
    if not cliente_encontrado:
        raise HTTPException(status_code=status.HPPT_400_BAD_REQUEST, detail=f"el cliente con id {cliente_id}, no existe")


@app.patch("/facturas/{id_factura}", response_model=Factura)
async def editar_facturas(id_factura: int, datos_factura: Factura):
    pass  

@app.delete("/facturas/{id_factura}", response_model=Factura)
async def eliminar_facturas(id_factura: int, datos_factura: Factura):
    pass  
