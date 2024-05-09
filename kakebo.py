from datetime import date
from enum import Enum

class Movimiento:
    def __init__(self, concepto, fecha, cantidad):
        self.concepto = concepto
        self.fecha = fecha
        self.cantidad = cantidad

        self.validar_tipos()
        self.validar_inputs()
        
    def validar_tipos(self):
        if not isinstance(self.concepto, str):
            raise TypeError("Concepto debe ser cadena de texto.")

        if not isinstance(self.fecha, date):
            raise TypeError("Fecha debe ser de tipo date.")
        
        if not (isinstance(self.cantidad, float) or isinstance(self.cantidad, int)):
            raise TypeError("Cantidad debe ser numerica.")

    def validar_inputs(self):
        if self.cantidad == 0:
            raise ValueError("La cantidad no puede ser 0")
        if len(self.concepto) < 5:
            raise ValueError("El concepto no puede estar vacio, o menor de 5 caracteres")   
        if self.fecha > date.today():
            raise ValueError("La fecha no puede ser posterior al dia de hoy")      
        
    def __repr__(self):
        return f"Movimiento: {self.fecha} {self.concepto} {self.cantidad:.2f}"

class Ingreso(Movimiento):     
    def __repr__(self):
        return f"Ingreso: {self.fecha} {self.concepto} {self.cantidad:.2f}"
        
class Gasto(Movimiento):
    def __init__(self, concepto, fecha, cantidad, categoria):
        super().__init__(concepto, fecha, cantidad)

        self.categoria = categoria
        self.validar_categoria()

    def validar_categoria(self):
        if not isinstance(self.categoria, CategoriaGastos):
            raise TypeError("Categoria debe ser CategoriaGastos.")
        
    def __repr__(self):
        return f"Gasto ({self.categoria.name}): {self.fecha} {self.concepto} {self.cantidad:.2f}"

class CategoriaGastos(Enum):
    NECESIDAD = 1
    CULTURA = 2
    OCIO_VICIO = 3
    EXTRAS = 4