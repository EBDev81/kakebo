#como leer ficheros de texto
f = open("./kakebo/data/movimientos.dat", "r")
cabecera = f.readline()
print(cabecera)
for linea in f:
    print(linea, end="")
    print("::::::::::::::::::")
    print(linea.split(","))
f.close()