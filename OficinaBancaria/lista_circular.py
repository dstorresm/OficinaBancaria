from nodo import Nodo

class ListaCircular:
    """
    Implementa una cola circular utilizando nodos enlazados.

    Atributos:
        referencia (Nodo): Referencia al último nodo de la lista circular.

    Métodos:
        esta_vacia(): Verifica si la lista está vacía.
        encolar(cliente): Agrega un cliente al final de la lista.
        desencolar(): Elimina y retorna el cliente al frente de la lista.
        mostrar(): Devuelve una lista con la representación en cadena de los clientes en la cola.
    """

    def __init__(self):
        """
        Inicializa una lista circular vacía.
        """
        self.referencia = None

    def esta_vacia(self):
        """
        Verifica si la lista circular está vacía.

        Returns:
            bool: True si la lista está vacía, False en caso contrario.
        """
        return self.referencia is None

    def encolar(self, cliente):
        """
        Agrega un cliente al final de la lista circular.

        Args:
            cliente: Objeto cliente a agregar a la cola.
        """
        nuevo = Nodo(cliente)
        if self.esta_vacia():
            nuevo.siguiente = nuevo
            self.referencia = nuevo
        else:
            nuevo.siguiente = self.referencia.siguiente
            self.referencia.siguiente = nuevo
            self.referencia = nuevo

    def desencolar(self):
        """
        Elimina y retorna el cliente al frente de la lista circular.

        Returns:
            cliente: El cliente desencolado, o None si la lista está vacía.
        """
        if self.esta_vacia():
            return None
        primer_nodo = self.referencia.siguiente
        if self.referencia == primer_nodo:
            self.referencia = None
        else:
            self.referencia.siguiente = primer_nodo.siguiente
        return primer_nodo.cliente

    def mostrar(self):
        """
        Devuelve una lista con la representación en cadena de los clientes en la cola.

        Returns:
            list: Lista de cadenas que representan a los clientes en la cola.
        """
        elementos = []
        if self.esta_vacia():
            return elementos
        actual = self.referencia.siguiente
        while True:
            elementos.append(str(actual.cliente))
            actual = actual.siguiente
            if actual == self.referencia.siguiente:
                break
        return elementos