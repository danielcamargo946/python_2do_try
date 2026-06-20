from fastapi import FastAPI, HTTPException, status
from modelos.clientes import clientes, clientecrear, ClienteEditar
from modelos.facturas import Factura, FacturaCrear, FacturaEditar
from modelos.transacciones import Transaccion, TransaccionCrear, TransaccionEditar

app = FastAPI()

#modelo clientes (clase)

lista_clientes:list[clientes] = []
lista_facturas: list[Factura] = []
lista_transacciones: list[Transaccion] = []

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
    raise HTTPException(status_code=400, detail=f"el cliente con id {cliente_id}, no existe")
 
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
    raise HTTPException(status_code=400, 
                        detail=f"la factura con id {id_factura}, no existe")

@app.post("/facturas/{cliente_id}", response_model=Factura)
async def crear_facturas(cliente_id: int, datos_factura: FacturaCrear):
    #buscar el cliente
    cliente_encontrado = None
    for clientes in lista_clientes:
        if clientes.id == cliente_id:
            cliente_encontrado = clientes

    if not cliente_encontrado:
        raise HTTPException(status_code=400, 
                            detail=f"el cliente con id {cliente_id}, no existe")

    #validar datos factura
    factura_val = Factura.model_validate(datos_factura.model_dump())
    factura_val.cliente = cliente_encontrado
    
    factura_val.id = len(lista_facturas)+1
    lista_facturas.append(factura_val)
    return factura_val


@app.patch("/facturas/{id_factura}", response_model=Factura)
async def editar_facturas(id_factura: int, datos_factura: Factura):
    pass  

@app.delete("/facturas/{id_factura}", response_model=Factura)
async def eliminar_facturas(id_factura: int, datos_factura: Factura):
    pass  

#====================================================================================================
#transacciones

@app.get("/transacciones/", response_model=Transaccion)
async def listar_transacciones():
    return lista_transacciones

@app.get("/transacciones/", response_model=Transaccion)
async def listar_transaccion():
    pass

#crear transaccion
@app.post("/transacciones/{factura_id}", response_model=Transaccion)
async def crear_transaccion(factura_id: int, datos_transaccion: TransaccionCrear):
    #buscar factura
    factura_encontrada = None
    for factura in lista_facturas:
        if factura.id == factura_id:
            factura_encontrada = factura

    if not factura_encontrada:
        raise HTTPException(status_code=400, 
                            detail=f"la factura con id {factura_id}, no existe")

    #validar datos factura
    transaccion_val = Transaccion.model_validate(datos_transaccion.model_dump())
    transaccion_val.factura_id = factura_id
    factura_encontrada.transacciones.append(transaccion_val)
    
    transaccion_val.id = len(lista_transacciones) + 1
    return transaccion_val

@app.patch("/transacciones/", response_model=Transaccion)
async def editar_transaccion():
    pass

@app.delete("/transacciones/", response_model=Transaccion)
async def eliminar_transaccion():
    pass