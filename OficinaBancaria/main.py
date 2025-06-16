import tkinter as tk
from interfaz_banco import InterfazBanco

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazBanco(root)
    root.mainloop()