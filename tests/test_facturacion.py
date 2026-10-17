import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from facturacion import CalculadorTotales, ServicioFacturacion


class RepositorioFalso:
    def __init__(self):
        self.facturas = []

    def guardar(self, cliente, total):
        self.facturas.append((cliente, total))


class NotificadorFalso:
    def __init__(self):
        self.notificaciones = []

    def enviar(self, email, total):
        self.notificaciones.append((email, total))


class TestFacturacion(unittest.TestCase):

    def test_calcula_total_con_impuesto_ilustrativo(self):
        calculador = CalculadorTotales(tasa_impuesto=0.19)
        productos = [{"nombre": "Producto A", "precio": 100.0}]

        self.assertEqual(calculador.calcular(productos), 119.0)

    def test_servicio_guarda_y_notifica(self):
        calculador = CalculadorTotales(tasa_impuesto=0.10)
        repositorio = RepositorioFalso()
        notificador = NotificadorFalso()

        servicio = ServicioFacturacion(
            calculador, repositorio, notificador
        )

        cliente = {
            "nombre": "Cliente de prueba",
            "email": "cliente@example.com"
        }
        productos = [{"nombre": "Producto A", "precio": 100.0}]

        total = servicio.procesar(cliente, productos)

        self.assertEqual(total, 110.0)
        self.assertEqual(repositorio.facturas, [(cliente, 110.0)])
        self.assertEqual(
            notificador.notificaciones,
            [("cliente@example.com", 110.0)]
        )

    def test_tasa_negativa_no_es_permitida(self):
        with self.assertRaises(ValueError):
            CalculadorTotales(tasa_impuesto=-0.1)

    def test_rechaza_precios_negativos(self):
        calculador = CalculadorTotales()
        productos = [{"nombre": "Producto A", "precio": -10.0}]

        with self.assertRaises(ValueError):
            calculador.calcular(productos)

    def test_rechaza_factura_sin_productos(self):
        calculador = CalculadorTotales()

        with self.assertRaises(ValueError):
            calculador.calcular([])


if __name__ == "__main__":
    unittest.main()