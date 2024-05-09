"""
1. Pedir si es ingreso o gasto o salir
2. Si es ingreso
    2.1 Pedir concepto
    2.2 Pedir fecha
    2.3 Pedir cantidad
3. Si es gastos
    3.1 Pedir concepto
    3.2 Pedir fecha
    3.3 Pedir cantidad
    3.4 Pedir categoria
3.5 Si es salir salimos a 7
4. Instancir el movimiento (ingreso o gasto)
5. Almacenar el movimiento en una lista
6. volver a 1

7. Procesar la lista de movimientos para obtener total de ingresos, gastos y saldo final
"""
from re import I
from kakebo import Ingreso, Gasto, CategoriaGastos
from datetime import date

listaMovimientos = []
listaIngresos = []
listaGastos = []

def validarFecha(fecha):
    try:
        return date.fromisoformat(fecha) <= date.today()
    except ValueError:
        return False
    
def esFloatPositivo(cadena):
    try:
        numero = float(cadena)
        return numero > 0
    except ValueError: 
        return False 

def esEntero(cadena):
    try:
        int(cadena)
        return True
    except ValueError:
        return False

def esCategoriaValida(cadena):
    if esEntero(cadena):
        entero = int(cadena)
        return entero in [categoria.value for categoria in CategoriaGastos]
    else:
        return False

def inputConcepto():
    concepto = input("Concepto: ")
    while len(concepto) < 5:
        print("El concepto debe tener al menos 5 caracteres")
        concepto = input("Concepto: ")
    return concepto

def inputFecha():
    fecha = input("Fecha (YYYY-MM-DD): ") 
    while not validarFecha(fecha):
        print("Introduzca una fecha valida (YYYY-MM-DD) y no futura")
        fecha = input("Fecha (YYYY-MM-DD): ")
    fecha = date.fromisoformat(fecha)
    return fecha

def inputCantidad():
    cantidad = input("Cantidad: " )
    while not esFloatPositivo(cantidad):
        print("Introduce un número positivo: ")
    cantidad = float(cantidad)
    return cantidad

def inpuCategoria():
    print("Lista de categorías de gastos:")
    for categoria in CategoriaGastos:#este for imprime la clase categoriaGastos de forma que el usuario la entienda
        print(f'{categoria.value} - {categoria.name}')
    cat = input("Elige el número de una de ellas: ")
    while not esCategoriaValida(cat):
        print("Has elegido una opción incorrecta")
        print("Lista de categorías de gastos:")
        for categoria in CategoriaGastos:#este for imprime la clase categoriaGastos de forma que el usuario la entienda
            print(f'{categoria.value} - {categoria.name}')
        cat = input("Elige el número de una de ellas: ")
    cat = CategoriaGastos(int(cat))
    return cat

def obtenerTotal(lista):
    total = 0
    for movimiento in lista:
        total += movimiento.cantidad
    return total

def obtenerTotales(lista):
    totalIngresos = 0
    totalGastos = 0
    saldo = 0

    for movimiento in lista:
        if isinstance(movimiento, Ingreso):
            totalIngresos += movimiento.cantidad
            saldo += movimiento.cantidad
        elif isinstance(movimiento, Gasto):
            totalGastos =+ movimiento.cantidad
            saldo -= movimiento.cantidad

    return totalIngresos, totalGastos, saldo

continuar = True
while continuar: 

    tipo = input("Ingreso, Gasto o Salir (I/G/S): ").lower()

    while tipo not in ('i', 'g', 's'):
        print("Teclea I, G o S")
        tipo = input("Ingreso, Gasto o Salir (I/G/S)").lower()

    if tipo == 'i':
        concepto = inputConcepto()
        fecha = inputFecha()
        cantidad = inputCantidad()

        mov = Ingreso(concepto, fecha, cantidad)
        listaIngresos.append(Ingreso(concepto, fecha, cantidad))
        listaMovimientos.append(listaIngresos[-1])

    elif tipo =="g":
        concepto = inputConcepto()
        fecha = inputFecha()
        cantidad = inputCantidad()
        categoria = inpuCategoria()

        mov = Gasto(concepto, fecha, cantidad, categoria)
        listaGastos.append(Gasto(concepto, fecha, cantidad, categoria))
        listaMovimientos.append(listaGastos[-1])

    elif tipo == "s":
        continuar = False

totalIngresos = obtenerTotal(listaIngresos)
totalGastos = obtenerTotal(listaGastos)
saldo = totalIngresos - totalGastos


print("VERSION DOS LISTAS")
print(f"Ingresos totales: {totalIngresos} €")
print(f"Gastos totales  : {totalGastos} €")
print("")
print(f"Ingresos: {totalIngresos:10.2f} €")
print(f"Gastos  : {totalGastos:10.2f} €")
print(f"Saldo   : {saldo:10.2f} €")

#VERSION UNA LISTA

totalI, totalG, saldoTotal = obtenerTotales(listaMovimientos)
print("")
print("VERSION UNA LISTA")
print(f"Ingresos: {totalI:10.2f} €")
print(f"Gastos..: {totalG:10.2f} €")
print(f"Saldo...: {saldoTotal:10.2f} €")