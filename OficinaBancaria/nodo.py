class Nodo:
    """
    Representa un nodo en una lista enlazada circular para almacenar clientes.

    Atributos:
        cliente: Objeto cliente almacenado en el nodo.
        siguiente (Nodo): Referencia al siguiente nodo en la lista.
    """

    def __init__(self, cliente):
        """
        Inicializa un nodo con un cliente y sin siguiente nodo.

        Args:
            cliente: Objeto cliente a almacenar en el nodo.
        """
        self.cliente = cliente