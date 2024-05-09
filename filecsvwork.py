#como leer ficheros csv normal
from main import *
from kakebo import *
import csv

print("::::::::::::::::::")
print("CSV NORMAL DEVUELVE LISTAS")
f = open("./Ingenieria_de_software/reposdepruebas/kakebo/data/movimientos.dat", "r")
reader = csv.reader(f, delimiter=",", quotechar='"')
for registro in reader:
    print(registro)
f.close()

#reader de tipo diccionario
print("::::::::::::::::::")
print("CSV DICT DEVUELVE LISTAS")

f = open("./Ingenieria_de_software/reposdepruebas/kakebo/data/movimientos.dat", "r")
reader = csv.DictReader(f, delimiter=",", quotechar='"')
for registro in reader:
    print(registro)
f.close()


#fatima
f = open("./data/movimientos.dat", "r")
reader = csv.DictReader(f, delimiter=",", quotechar='"')
for registro in reader:
    print(registro)
    categoria = registro["categoria"]
    if categoria == "":
        movimiento = Ingreso(registro["concepto"], date.fromisoformat(registro["fecha"]), float(registro["cantidad"]))
    elif categoria != "":
        movimiento = Gasto(registro["concepto"], date.fromisoformat(registro["fecha"]), float(registro["cantidad"]), CategoriaGastos(int(registro["categoria"])))
    print(movimiento) 

f.close()