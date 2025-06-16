import random

class Cliente:
    """
    Representa un cliente de la oficina bancaria.

    Atributos:
        id (int): Identificador único del cliente.
        transacciones (int): Número de transacciones pendientes del cliente.

    Métodos:
        realizar_transacciones(cantidad): Realiza una cantidad de transacciones, hasta el máximo disponible.
        tiene_pendientes(): Indica si el cliente tiene transacciones pendientes.
        __str__(): Devuelve una representación en cadena del cliente.
    """

    def __init__(self, id_cliente):
        """
        Inicializa un nuevo cliente con un identificador y un número aleatorio de transacciones pendientes.

        Args:
            id_cliente (int): Identificador único del cliente.
        """
        self.id = id_cliente
        self.transacciones = random.randint(15, 30)

    def realizar_transacciones(self, cantidad):
        """
        Realiza hasta 'cantidad' transacciones, dependiendo de las transacciones pendientes.

        Args:
            cantidad (int): Número máximo de transacciones a realizar.

        Returns:
            int: Número de transacciones realmente realizadas.
        """
        realizadas = min(self.transacciones, cantidad)
        self.transacciones -= realizadas
        return realizadas

    def tiene_pendientes(self):
        """
        Verifica si el cliente tiene transacciones pendientes.

        Returns:
            bool: True si quedan transacciones pendientes, False en caso contrario.
        """
        return self.transacciones > 0

    def __str__(self):
        """
        Devuelve una representación en cadena del cliente.

        Returns:
            str: Representación del cliente y sus transacciones restantes.
        """
        return f"Cliente {self.id} - Transacciones restantes: {self.transacciones}"