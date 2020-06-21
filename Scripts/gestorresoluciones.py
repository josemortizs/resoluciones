# -*- coding: utf-8 -*-

# Copyright (C) 2020  ortizsanchezdev

# Author: José Manuel Ortiz Sánchez <josemortizs@gmail.com>
# Maintainer: José Manuel Ortiz Sánchez <josemortizs@gmail.com>

# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with urls; see the file LICENSE.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,


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