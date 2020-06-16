# -*- coding: utf-8 -*-
# Importamos la clase Resolucion()
""" Al tener que ser importada, la clase GestorResoluciones() desde init.py, me veo obligado 
    a modicar la ruta de la importación para hacerla correctamente desde init.py
"""
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
        datosFichero = open(file="Data/DatosGestorResoluciones.csv", mode="r+", encoding="utf-8")
        contenido = csv.reader(datosFichero)
        for resolucion in contenido:
           self.resoluciones.append(Resolucion(int(resolucion[0]), int(resolucion[1]), resolucion[2], resolucion[3]))
        datosFichero.close()
    

    def agregaResolucion(self, resolucion):
        if isinstance(resolucion, Resolucion):
            self.resoluciones.append(resolucion)
        else:
            print("No puedes agregar un objeto que no sea de tipo Resolucion()")
    
    def imprimeListadoResoluciones(self):
        for resolucion in self.resoluciones:
            print(resolucion)

# ---------------------------------------------------------------------------------------------------------------------