from tkinter import *
from tkinter import ttk
from guardaresoluciones import GuardaResoluciones


class ResolucionesUI():

    def __init__(self):

        # Declaramos y configuramos la vista
        self.raiz = Tk()
        self.raiz.geometry('600x100')
        self.raiz.resizable(0,0)
        self.raiz.configure(bg='beige')
        self.raiz.title('Resoluciones')

        # Declaramos las variables de control
        self.url = StringVar(value='https://www.ortizsanchezdev.es')

        # Declaramos los widgets asociados a la vista
        self.inputURL = ttk.Entry(self.raiz, textvariable=self.url, width=10)
        self.btnCargar = ttk.Button(self.raiz, text="Cargar", command=self.cargarResoluciones)
        self.btnSalir = ttk.Button(self.raiz, text="Salir", command=quit)

        # Posicionamos los widgets dentro de la vista
        self.inputURL.pack(side=TOP, fill=BOTH, expand=False, padx=10, pady=10)
        self.btnCargar.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)
        self.btnSalir.pack(side=RIGHT, fill=BOTH, expand=True, padx=10, pady=10)

        self.raiz.mainloop()
    
    def cargarResoluciones(self):
        urlCR = str(self.url.get())
        print(urlCR)
        resoluciones = GuardaResoluciones(urlCR)

# ---------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    ui = ResolucionesUI()
