# -*- coding: utf-8 -*-
# Importamos la clase Resolucion()
from resolucion import Resolucion
# Importamos la librería "csv" para trabajar con este tipo de archivos
import csv

class GestorResoluciones():

    """ **************************************************************** 
    Clase creada para la gestión de resoluciones

    Contendrá una lista de objetos de tipo Resolucion y métodos
    orientados a la inserción, edición y elimnación de éstas. 
    Recuperará, y almacenará, las resoluciones mediante ficheros CSV
    *************************************************************** """ 

    # Constructor
    def __init__(self):
        self.resoluciones = [] # Lista de objetos de tipo Resolucion
        self.recuperaResoluciones() # Método para la carga inicial de las resoluciones
    

    # Métodos de instancia
    def recuperaResoluciones(self):
        datosGestorResoluciones = open(file="Data/DatosGestorResoluciones.csv", mode="r+", encoding="utf-8")
        contenido = csv.reader(datosGestorResoluciones)
        for resolucion in contenido:
           self.resoluciones.append(Resolucion(int(resolucion[0]), int(resolucion[1]), resolucion[2], resolucion[3]))
        datosGestorResoluciones.close()
    

    def agregaResolucion(self, resolucion):
        if isinstance(resolucion, Resolucion):
            self.resoluciones.append(resolucion)
            self.guardaResolucion(resolucion)
        else:
            print("No puedes agregar un objeto que no sea de tipo Resolucion()")
    

    def guardaResolucion(self, resolucion):
        datosGestorResoluciones = open(file="Data/DatosGestorResoluciones.csv", mode="a", encoding="utf-8")
        contenido = csv.writer(datosGestorResoluciones)
        contenido.writerow([resolucion.ancho, resolucion.alto, resolucion.tipo, resolucion.nombre])
        datosGestorResoluciones.close()

    
    def imprimeListadoResoluciones(self):
        for resolucion in self.resoluciones:
            print(resolucion)

# ---------------------------------------------------------------------------------------------------------------------