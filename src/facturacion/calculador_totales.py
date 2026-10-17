class CalculadorTotales:
    """Calcula el total de una lista de productos."""

    def __init__(self, tasa_impuesto: float = 0.19):
        if tasa_impuesto < 0:
            raise ValueError("La tasa de impuesto no puede ser negativa.")

        self.tasa_impuesto = tasa_impuesto

    def calcular(self, productos: list[dict]) -> float:
        for producto in productos:
            precio = float(producto["precio"])

            if precio < 0:
                raise ValueError("El precio no puede ser negativo.")

        subtotal = sum(float(producto["precio"]) for producto in productos)

        return round(subtotal * (1 + self.tasa_impuesto), 2)