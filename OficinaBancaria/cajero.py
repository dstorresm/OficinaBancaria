class Cajero:
    """
    Representa un cajero en una oficina bancaria.

    Atributos:
        ocupado (bool): Indica si el cajero está ocupado atendiendo a un cliente.

    Métodos:
        atender_cliente(cliente): Atiende a un cliente permitiéndole realizar transacciones.
    """

    def __init__(self):
        """
        Inicializa un nuevo cajero como desocupado.
        """
        self.ocupado = False

    def atender_cliente(self, cliente):
        """
        Atiende a un cliente permitiéndole realizar hasta 5 transacciones.

        Args:
            cliente: Objeto que representa al cliente a atender. Debe tener el método realizar_transacciones.

        Returns:
            El resultado de cliente.realizar_transacciones(5).
        """
        return cliente.realizar_transacciones(5)