import tkinter as tk
from tkinter import ttk
from simulador_banco import SimuladorBanco
import random

class InterfazBanco:
    """
    Interfaz gráfica para la simulación de una oficina bancaria usando Tkinter.

    Atributos:
        root (tk.Tk): Ventana principal de la aplicación.
        simulador (SimuladorBanco): Instancia del simulador de banco.
        tiempo_simulado (int): Tiempo simulado en segundos.
        frame (ttk.Frame): Marco principal de la interfaz.
        label_tiempo (ttk.Label): Etiqueta que muestra el tiempo simulado.
        label_cola (ttk.Label): Etiqueta que indica los clientes en espera.
        lista_clientes (tk.Listbox): Lista de clientes en espera.
        resultado (tk.StringVar): Variable para mostrar mensajes de resultado.
        label_resultado (ttk.Label): Etiqueta para mostrar el resultado de acciones.
        btn_turno (ttk.Button): Botón para procesar un turno.
        label_estadisticas (ttk.Label): Etiqueta para mostrar estadísticas.

    Métodos:
        actualizar_lista(): Actualiza la lista de clientes en la interfaz.
        procesar_turno(): Procesa un turno en el simulador y actualiza la interfaz.
        mostrar_resumen(): Muestra un resumen de la simulación.
        programar_cliente_automatico(): Agrega clientes automáticamente en intervalos aleatorios.
        actualizar_reloj(): Actualiza el tiempo simulado cada segundo.
        actualizar_estadisticas(): Actualiza las estadísticas mostradas en la interfaz.
    """

    def __init__(self, root):
        """
        Inicializa la interfaz gráfica y sus componentes.

        Args:
            root (tk.Tk): Ventana principal de la aplicación.
        """
        self.root = root
        self.root.title("Simulación de Oficina Bancaria")
        self.root.geometry("600x550")

        self.simulador = SimuladorBanco()
        self.simulador.generar_clientes_iniciales()

        self.tiempo_simulado = 0  # en segundos

        self.frame = ttk.Frame(self.root, padding="10")
        self.frame.pack(fill="both", expand=True)

        self.label_tiempo = ttk.Label(self.frame, text="Tiempo simulado: 0s", font=("Arial", 10))
        self.label_tiempo.pack(pady=2)

        self.label_cola = ttk.Label(self.frame, text="Clientes en espera:")
        self.label_cola.pack()

        self.lista_clientes = tk.Listbox(self.frame, height=10, width=70)
        self.lista_clientes.pack(pady=5)

        self.resultado = tk.StringVar()
        self.label_resultado = ttk.Label(self.frame, textvariable=self.resultado, foreground="blue", font=("Arial", 11))
        self.label_resultado.pack(pady=10)

        self.btn_turno = ttk.Button(self.frame, text="Procesar Turno", command=self.procesar_turno)
        self.btn_turno.pack(pady=5)

        self.label_estadisticas = ttk.Label(self.frame, text="", font=("Arial", 10))
        self.label_estadisticas.pack(pady=5)

        self.actualizar_lista()
        self.programar_cliente_automatico()
        self.actualizar_reloj()

    def actualizar_lista(self):
        """
        Actualiza la lista de clientes en espera en la interfaz gráfica.
        """
        self.lista_clientes.delete(0, tk.END)
        for cliente_str in self.simulador.obtener_estado_cola():
            self.lista_clientes.insert(tk.END, cliente_str)
        self.actualizar_estadisticas()

    def procesar_turno(self):
        """
        Procesa un turno en el simulador, actualiza la lista de clientes y muestra el resultado.
        """
        mensaje = self.simulador.procesar_turno()
        self.resultado.set(mensaje)
        self.actualizar_lista()

    def mostrar_resumen(self):
        """
        Muestra un resumen de la simulación en la interfaz.
        """
        resumen = self.simulador.resumen()
        self.resultado.set(resumen)

    def programar_cliente_automatico(self):
        """
        Agrega un nuevo cliente automáticamente en intervalos aleatorios y actualiza la interfaz.
        """
        self.simulador.agregar_cliente()
        self.actualizar_lista()
        self.resultado.set("Nuevo cliente agregado automáticamente.")
        intervalo = random.randint(3000, 7000)
        self.root.after(intervalo, self.programar_cliente_automatico)

    def actualizar_reloj(self):
        """
        Incrementa el tiempo simulado y actualiza la etiqueta correspondiente cada segundo.
        """
        self.tiempo_simulado += 1
        self.label_tiempo.config(text=f"Tiempo simulado: {self.tiempo_simulado}s")
        self.root.after(1000, self.actualizar_reloj)

    def actualizar_estadisticas(self):
        """
        Actualiza las estadísticas de clientes atendidos y transacciones procesadas en la interfaz.
        """
        texto = f"Clientes atendidos: {self.simulador.total_clientes_atendidos} | Transacciones procesadas: {self.simulador.total_transacciones}"
        self.label_estadisticas.config(text=texto)