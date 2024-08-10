# aplicacion de gestion de gimnasios


class Cliente:
    def __init__(self,id_cliente,nombre,edad,telefono):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
        self.membresias = []

    def agregar_membresia(self,membresia):
        self.membresias.append(membresia)

class Membresia:
    def __init__(self,id_membresia,tipo,costo,duracion_meses):
        self.id_membresia = id_membresia
        self.tipo = tipo
        self.costo = costo
        self.duracion_meses = duracion_meses
        self.activa = True
    
    def cancelar(self):
        self.activa = False
    
class Pago:
    def __init__(self,id_pago,id_cliente,monto,fecha):
        self.id_pago = id_pago
        self.id_cliente = id_cliente
        self.monto = monto
        self.fecha = fecha

class Gimnasio:
    def __init__(self):
        self.clientes = []
        self.membresias = []
        self.pagos = []

    def registrar_cliente(self,cliente):
        self.clientes.append(cliente)
    
    def registrar_membresia(self,membresia,id_cliente):
        cliente = self.buscar_cliente(id_cliente)
        if cliente:
            cliente.agregar_membresia(membresia)
            self.membresias.append(membresia)
    
    def registrar_pago(self,pago):
        self.pagos.append(pago)
    
    def buscar_cliente(self,id_cliente):
        for cliente in self.clientes:
            if cliente.id_cliente == id_cliente:
                return cliente
        return None
    
    def generar_informe(self):
        clientes_atendidos = len(self.clientes)
        ingresos_generados = sum(pago.monto for pago in self.pagos)
        return {
            "clientes_atendidos" : clientes_atendidos,
            "ingresos_generados" : ingresos_generados,
            "pagos_realizados" : len(self.pagos)

    

        }
    
gimnasio = Gimnasio()

cliente1 = Cliente(id_cliente=1,nombre="Sebastian Gomez", edad=36,telefono=6750444)
cliente2 = Cliente(id_cliente=2,nombre="Nicolas Gomez", edad=30,telefono=6750555)

gimnasio.registrar_cliente(cliente1)
gimnasio.registrar_cliente(cliente2)

membresia1 = Membresia(id_membresia=1,tipo="Mensual",costo=50,duracion_meses=1)
membresia2 = Membresia(id_membresia=2,tipo="Anual",costo=500,duracion_meses=12)

gimnasio.registrar_membresia(membresia1,id_cliente=1)
gimnasio.registrar_membresia(membresia2,id_cliente=2)

pago1 = Pago(id_pago=1,id_cliente=1,monto=50,fecha="2024-05-27")
pago2 = Pago(id_pago=2,id_cliente=2,monto=500,fecha="2024-05-27")

gimnasio.registrar_pago(pago1)
gimnasio.registrar_pago(pago2)

informe = gimnasio.generar_informe()

print(informe)