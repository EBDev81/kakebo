from datetime import date
from kakebo import Ingreso, CategoriaGastos, Gasto
import pytest

def test_instanciar_ingreso():
    movimiento = Ingreso("Loteria del niño, premio", date(2024, 1, 1), 1000)

    assert movimiento.concepto == "Loteria del niño, premio"
    assert movimiento.fecha == date(2024, 1, 1)
    assert movimiento.cantidad == 1000

def test_ingreso_concepto_debe_ser_string():
    with pytest.raises(TypeError):
        movimiento = Ingreso(19, date(2024, 1, 5), 1000)

def test_ingreso_fecha_debe_ser_date():
    with pytest.raises(TypeError):
        movimiento = Ingreso("Loteria del niño, premio", "lolailo", 1000)

def test_ingreso_cantidad_debe_ser_float_o_int():
    with pytest.raises(TypeError):
        movimiento = Ingreso("Loteria del niño, premio", date(2024, 1, 5), "casa")

    movimiento = Ingreso("indiferente", date.today(), 1000)
    movimiento = Ingreso("indiferente", date.today(), 1000.1)

def test_concepto_min_5_caracteres():
    with pytest.raises(ValueError):
        movimiento = Ingreso("indi", date(2024, 4, 30), 1)

def test_ingreso_fecha_no_futura():
    with pytest.raises(ValueError):
        movimiento = Ingreso("Salario", date(3000, 1, 1), 1000)

def test_cantidad_no_debe_ser_cero():
    with pytest.raises(ValueError):
        movimiento = Ingreso("Loteria del niño, premio", date.today(), 0)

def test_crear_gasto():
    movimiento = Gasto("Factura del agua", date(2024, 4, 30), 70, CategoriaGastos.NECESIDAD)
   
    assert movimiento.concepto == "Factura del agua"
    assert movimiento.fecha == date(2024, 4, 30)
    assert movimiento.cantidad == 70
    assert movimiento.categoria == CategoriaGastos.NECESIDAD

def test_gasto_categoria_tipo_correcto():
    with pytest.raises(TypeError):
        movimiento = Gasto("Factura del agua", date(2024, 4, 30), 70, "Necesidad")