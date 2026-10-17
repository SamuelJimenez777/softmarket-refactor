class CalculadorTotales:
    """Calcula el total de una lista de productos con una tasa ilustrativa."""

    def __init__(self, tasa_impuesto: float = 0.19):
        if tasa_impuesto < 0:
            raise ValueError("La tasa de impuesto no puede ser negativa.")
        self.tasa_impuesto = tasa_impuesto

    def calcular(self, productos: list[dict]) -> float:
        subtotal = sum(float(producto["precio"]) for producto in productos)
        return round(subtotal * (1 + self.tasa_impuesto), 2)
