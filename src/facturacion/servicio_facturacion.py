class ServicioFacturacion:
    """Coordina el cálculo, el almacenamiento y la notificación de una factura.

    repositorio debe implementar guardar(cliente, total).
    notificador debe implementar enviar(email, total).
    """

    def __init__(self, calculador, repositorio, notificador):
        self.calculador = calculador
        self.repositorio = repositorio
        self.notificador = notificador

    def procesar(self, cliente: dict, productos: list[dict]) -> float:
        total = self.calculador.calcular(productos)
        self.repositorio.guardar(cliente, total)
        self.notificador.enviar(cliente["email"], total)
        return total
