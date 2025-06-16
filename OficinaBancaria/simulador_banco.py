from cliente import Cliente
from lista_circular import ListaCircular
from cajero import Cajero
import random

class SimuladorBanco:
    """
    Simula la atención de clientes en una oficina bancaria con un cajero y una cola circular.

    Atributos:
        cola (ListaCircular): Cola circular de clientes en espera.
        cajero (Cajero): Cajero encargado de atender a los clientes.
        id_contador (int): Contador para asignar identificadores únicos a los clientes.
        total_clientes_atendidos (int): Número total de clientes completamente atendidos.
        total_transacciones (int): Número total de transacciones procesadas.

    Métodos:
        generar_clientes_iniciales(): Genera una cantidad aleatoria de clientes iniciales y los agrega a la cola.
        agregar_cliente(): Agrega un nuevo cliente a la cola.
        procesar_turno(): Atiende al siguiente cliente en la cola y actualiza las estadísticas.
        obtener_estado_cola(): Devuelve una lista con el estado actual de la cola.
        resumen(): Devuelve un resumen de la simulación.
    """

    def __init__(self):
        """
        Inicializa el simulador con una cola vacía, un cajero y contadores en cero.
        """
        self.cola = ListaCircular()
        self.cajero = Cajero()
        self.id_contador = 1
        self.total_clientes_atendidos = 0
        self.total_transacciones = 0

    def generar_clientes_iniciales(self):
        """
        Genera una cantidad aleatoria de clientes iniciales y los agrega a la cola.
        """
        cantidad = random.randint(3, 10)
        for _ in range(cantidad):
            self.agregar_cliente()

    def agregar_cliente(self):
        """
        Crea un nuevo cliente con un identificador único y lo agrega a la cola.
        """
        cliente = Cliente(self.id_contador)
        self.cola.encolar(cliente)
        self.id_contador += 1

    def procesar_turno(self):
        """
        Atiende al siguiente cliente en la cola, procesa sus transacciones y actualiza las estadísticas.

        Returns:
            str: Mensaje con el resultado de la atención al cliente.
        """
        if self.cola.esta_vacia():
            return "No hay clientes en espera."

        cliente = self.cola.desencolar()
        transacciones_procesadas = self.cajero.atender_cliente(cliente)
        self.total_transacciones += transacciones_procesadas

        mensaje = f"Cliente {cliente.id}: {transacciones_procesadas} transacciones atendidas."

        if cliente.tiene_pendientes():
            self.cola.encolar(cliente)
            mensaje += f" Transacciones restantes: {cliente.transacciones} (regresó a la cola)"
        else:
            self.total_clientes_atendidos += 1
            mensaje += " Todas sus transacciones han sido atendidas."

        return mensaje

    def obtener_estado_cola(self):
        """
        Obtiene el estado actual de la cola de clientes.

        Returns:
            list: Lista de cadenas que representan a los clientes en la cola.
        """
        return self.cola.mostrar()

    def resumen(self):
        """
        Devuelve un resumen de la simulación.

        Returns:
            str: Resumen de clientes atendidos y transacciones procesadas.
        """
        return f"Clientes totalmente atendidos: {self.total_clientes_atendidos}, Transacciones totales procesadas: {self.total_transacciones}"