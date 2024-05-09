"""
1. Pedir si es ingreso o gasto o salir
2. Si es ingreso:
    2.1 Pedir concepto
    2.2 Pedir fecha
    2.3 Pedir cantidad
3. Si es Gasto:
    3.1 Pedir concepto
    3.2 Pedir fecha
    3.3 Pedir cantidad
    3.4 Pedir categoria
3.5 si es salir salimos a 7.
4. Instanciar el movimiento (ingreso o gasto)
5. Almacenar el movimiento en una lista
6. Volver a 1.

7. Procesar la lista de movimientos para obtener total de ingresos, gastos y saldo final
"""
from kakebo import Ingreso, Gasto, CategoriaGastos
from datetime import date

listaMovimientos = [] #lista inicializada a cero para meter todos los movimientos

def validarFecha(fecha): #se encarga de que el formato sea correcto y que sea menor o igual a hoy.
    try:
        return date.fromisoformat(fecha) <= date.today()
    except ValueError:
        return False 

def imprimirMovimientos(): #imprime en pantalla todos los gastos e ingresos introducidos por el usuario una vez que haya selccionado el tipo "s" que es salir
    print("Movimientos registrados: ")
    for elemento in listaMovimientos:
        print(elemento)
    print("Fin de movimientos registrados")

def instanciarMovimiento(tipo, concepto, fecha, cantidad, categoria_elegida=""):#le pasa a la clase todos los datos para instanciar un movimiento   
    if tipo == "i":
        movimiento = Ingreso(concepto, fecha, cantidad)    
    if tipo == "g":
        movimiento = Gasto(concepto, fecha, cantidad, categoria_elegida)
    almacenarMovimiento(movimiento)#recibe el movimiento recién instanciado, y se lo pasa a la funcion almacenarMovimiento, para que todos estén registrados y disponibles en la lista al salir del proceso de crear nuevos movimientos

def almacenarMovimiento(movimiento):#almacena los movimientos en la lista que tenemos definida arriba
    listaMovimientos.append(movimiento)
    print("Movimiento registrado correctamente")

continuar = True #iniciamos continuar a True para poder cumplir con el punto "6. Volver a 1."
while continuar:  #como continuar es True, entramos en el bucle  
    tipo = input("Ingreso, Gasto o Salir (I/G/S): ").lower()

    while tipo not in ("i","g","s"): #bucle que valida que el tipo sea correcto
        print("Teclea I, G o S")
        tipo = input("Ingreso, Gasto o Salir (I/G/S): ").lower()

    if tipo == "i": #si el tipo es i(ingreso) 
        concepto = input("Concepto: ") #le pedimos el concepto y lo guardamos en una variable
        while len(concepto) < 5: #este bucle comprueba que el concepto sea superior a 5 caracteres
            print("El concepto debe tener al menos 5 carácteres")
            concepto = input("Concepto: ")
    
        fecha = input("Introduce la fecha del ingreso(YYYY-MM-DD): ")#pedimos fecha
        while not validarFecha(fecha): #comprobamos que el formato de la fecha sea correcta(el formato, no el tipo de dato)
            print("Introduzca una fecha válida (YYY-MM-DD) y NO FUTURA")
            fecha = input("Introduce la fecha del ingreso(YYYY-MM-DD): ") 
        fecha = date.fromisoformat(fecha) #pasamos la cadena fecha str a formato date

        while True: #iniciamos el bucle porque siempre inicia en true y solo parará cuando pase por el ultimo if y la cantidad sea mayor de cero 
            try:
                cantidad = float(input("Introduce la cantidad en numeros: "))
                if cantidad < 0: 
                    cantidad = float(input("Introduce una cantidad que sea mayor que cero: "))
                if cantidad == 0: 
                    cantidad = float(input("Introduce una cantidad que no sea cero: "))
                if cantidad > 0:
                    break
            except ValueError:
                print("Error: Por favor introduce la cantidad con números válidos y no letras ni símbolos.") 
        instanciarMovimiento(tipo, concepto, fecha, cantidad)#pasa los parametros recopilados a la funcion instanciarMovimiento

    if tipo == "g": #concepto fecha y cantidad funcionan igual que en "if tipo =="i""
        concepto = input("Concepto: ")
        while len(concepto) < 5:
            print("El concepto debe tener al menos 5 carácteres")
            tipo = input("Concepto: ")
    
        fecha = input("Introduce la fecha del gasto(YYYY-MM-DD): ")
        while not validarFecha(fecha):
            print("Introduzca una fecha válida (YYY-MM-DD) y NO FUTURA")
            fecha = input("Introduce la fecha del gasto(YYYY-MM-DD): ") 
        fecha = date.fromisoformat(fecha) #pasamos la cadena fecha str a formato date

        while True:
            try:
                cantidad = float(input("Introduce la cantidad en numeros: "))
                if cantidad < 0: 
                    break
                elif cantidad == 0: 
                    cantidad = float(input("Introduce una cantidad que no sea cero: "))
                else: 
                    cantidad *= -1
                    break
            except ValueError:
                print("Error: Por favor introduce la cantidad con números válidos y no letras ni símbolos.")        
#¡¡¡¡CATEGORIA NO COMPRUEBA SI METEN UN CARACTER Y NO UN NUMERO!!!!
        print("Lista de categorías de gastos:")
        for categoria in CategoriaGastos:#este for imprime la clase categoriaGastos de forma que el usuario la entienda
            print(f'{categoria.value} - {categoria.name}')
        while True: #este bucle comprueba que la categoria que introduce el usuario sea una de las categorias disponibles dentro de la clase categoriaGastos
            eleccion_usuario = int(input("Introduce el número de la categoría de gastos: "))
            if eleccion_usuario in [categoria.value for categoria in CategoriaGastos]:
                categoria_elegida = CategoriaGastos(eleccion_usuario)
                break
            else:
                print("El número introducido no corresponde a ninguna categoría válida.")
        instanciarMovimiento(tipo, concepto, fecha, cantidad, categoria_elegida)#pasa los parametros recopilados a la funcion instanciarMovimiento

    if tipo == "s": #si el tipo es "s" llamamos a la funcion imprimir movimientos y salimos del bucle "continuar"
        imprimirMovimientos() #ver info en la función
        continuar = False #pasamos continuar a false para salir del bucle

#ACABAR HASTA EL PUNTO 5 COMO RETO-> OK 
#RETO DE DISCORD in process