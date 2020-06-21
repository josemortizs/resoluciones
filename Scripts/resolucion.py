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

class Resolucion():
    
    """ **************************************************************** 
    Clase creada para la representación de una resolución de pantalla.

    Contiene las variables ancho y alto (propias de cada pantalla), así 
    como el tipo de pantalla (móvil, pc, tablet...) y un nombre 
    que puede usarse como identificador de cada resolución.
    *************************************************************** """ 

    # Constructor
    def __init__(self, ancho = 320, alto = 568, tipo = 'No especificado', nombre = 'No especificado'):
        self.ancho = ancho
        self.alto = alto
        self.tipo = tipo
        self.nombre = nombre
    

    # Getter
    @property
    def ancho(self):
        return self._ancho
    
    @property
    def alto(self):
        return self._alto
    

    # Setter
    @ancho.setter
    def ancho(self, ancho):
        self._ancho = ancho if (ancho >= 320) else 320
    
    @alto.setter
    def alto(self, alto):
        self._alto = alto if (alto >= 568) else 568
    
    # Sobreescribimos el método __str__
    def __str__(self):
        return "Nombre: {0} - Tipo: {1} - Resolución: {2} x {3}".format(self.nombre, self.tipo, self.ancho, self.alto)
    
    # Sobreescribimos el método __eq__ para poder comparar, correctamente, si dos objetos de la clase Resolucion son iguales
    def __eq__(self, otraResolucion):
        return ((self.ancho == otraResolucion.ancho) and (self.alto == otraResolucion.alto))
    
# ---------------------------------------------------------------------------------------------------------------------------