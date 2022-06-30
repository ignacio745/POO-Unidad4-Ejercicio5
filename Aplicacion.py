from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from turtle import back

class Aplicacion:
    __ventana=None
    def __init__(self) -> None:
        self.__ventana = Tk()
        self.__ventana.title("Calculadora de IMC")
        self.__altura = IntVar()
        self.__peso = IntVar()
        self.__imc = StringVar()
        self.__tipoPeso = StringVar()
        ops = dict(borderwidth=0, padding=(0, 0))
        self.__marco = ttk.Frame(self.__ventana, **ops)
        s = ttk.Style()
        s.configure('TFrame', background='white')
        s.configure('TButton', background = '#5cb85c', foreground = 'white')
        """self.__marcoTitulo = ttk.Frame(self.__ventana, **ops)
        self.__marcoAltura = ttk.Frame(self.__ventana, **ops)
        self.__marcoPeso = ttk.Frame(self.__ventana, **ops)
        self.__marcoBotones = ttk.Frame(self.__ventana, **ops)
        self.__marcoInforme = ttk.Frame(self.__ventana, **ops)"""
        self.__titulo = ttk.Label(self.__marco, text="Calculadora de IMC", padding=(200,5), background="#f5f5f5", foreground="black")
        self.__alturaLbl = ttk.Label(self.__marco, text="Altura: ", padding=(5,5), background="white", foreground="#787c85")
        self.__alturaEntry = ttk.Entry(self.__marco, textvariable=self.__altura, width=40)
        self.__alturaUnidad = ttk.Label(self.__marco, text="cm", padding=(5,5), background="#eeeeee", foreground="#787c85")
        self.__pesoLbl = ttk.Label(self.__marco, text="Peso: ", padding=(5,5), background="white", foreground="#787c85")
        self.__pesoEntry = ttk.Entry(self.__marco, textvariable=self.__peso, width=40)
        self.__pesoUnidad = ttk.Label(self.__marco, text="kg", padding=(5,5), background="#eeeeee", foreground="#787c85")
        self.__botonCalcular = ttk.Button(self.__marco, text="Calcular", command=self.calcular)
        self.__botonLimpiar = ttk.Button(self.__marco, text="Limpiar", command=self.limpiar)
        self.__informe = ttk.Label(self.__marco, textvariable=self.__imc, background="#dff0d8", foreground="#408267")
        self.__informe2 = ttk.Label(self.__marco, textvariable=self.__tipoPeso, background="#dff0d8", foreground="#408267")
        self.__marco.grid(column=0, row=0)
        self.__titulo.grid(column=0, row=0, columnspan=3)
        self.__alturaLbl.grid(column=0, row=1, sticky="w")
        self.__alturaEntry.grid(column=1, row=1)
        self.__alturaUnidad.grid(column=2, row=1, sticky="nswe")
        self.__pesoLbl.grid(column=0, row=2, sticky="w")
        self.__pesoEntry.grid(column=1, row=2)
        self.__pesoUnidad.grid(column=2, row=2, sticky="nswe")
        self.__botonCalcular.grid(column=0, row=3)
        self.__botonLimpiar.grid(column=2, row=3)
        self.__informe.grid(column=1, row=4)
        self.__informe2.grid(column=1, row=5)
        cols, rows = self.__ventana.grid_size()
        for col in range(cols):
            self.__ventana.grid_columnconfigure(col, weight=800)
        for row in range(rows):
            self.__ventana.grid_rowconfigure(row)
        self.__ventana.mainloop()
    


    def calcular(self):
        try:
            altura = self.__altura.get() / 100
        except TclError:
            messagebox.showerror(title="Altura invalida", message="Debe ingresar un valor entero")
            self.limpiar()
            return

        try:
            peso = self.__peso.get()
        except TclError:
            messagebox.showerror(title="Peso invalido", message="Debe ingresar un valor entero")
            self.limpiar()
            return
            
        try:
            imc = peso / altura**2
        except ZeroDivisionError:
            self.limpiar()
            self.__imc.set("La altura no puede ser 0")
            return
        
        self.__imc.set("Tu indice de Masa Corporal (IMC) es {0:.2f} Kg/m2".format(imc))
        if imc < 18.5:
            self.__tipoPeso.set("Peso inferior al normal")
        elif 18.5 <= imc < 25:
            self.__tipoPeso.set("Peso normal")
        elif 25 <= imc < 30:
            self.__tipoPeso.set("Peso superior al normal")
        else:
            self.__tipoPeso.set("Obesidad")


    


    def limpiar(self):
        self.__altura.set(0)
        self.__peso.set(0)
        self.__imc.set("")
        self.__tipoPeso.set("")