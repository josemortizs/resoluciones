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


# Sección de importaciones:
from resolucion import Resolucion
from selenium import webdriver
import threading 
import os



class GuardarWebEnResolucion(threading.Thread):

    """ **************************************************************** 
    Clase creada para guardar una captura de pantalla, de una url, a una
    determinada resolución.

    Hereda de la clase Thread, del paquete threading, que se usa para el 
    manejo de "hilos"

    Contiene las variables de instancia url, de tipo str, y resolución,
    instancia de la clase Resolucion()
    *************************************************************** """

    # Constructor
    def __init__(self, url = '', resolucion = Resolucion(320, 568, 'No especificado', 'No especificado')):
        threading.Thread.__init__(self)
        self.url = url
        self.resolucion = resolucion
        self.eventoHilo = threading.Event()

    
    def run(self):
        nombreImagen = "{0}x{1}_{2}_{3}".format(self.resolucion.ancho, self.resolucion.alto, self.resolucion.tipo, self.resolucion.nombre)
        rutaImagen = os.path.abspath('..\Screenshot')
        rutaCompleta = "{0}\{1}.png".format(rutaImagen, nombreImagen)
        driver = webdriver.Chrome(executable_path=r'C:/chromedriver/windows/chrome83/chromedriver.exe')
        driver.set_window_size(self.resolucion.ancho, self.resolucion.alto)
        driver.get(self.url)
        driver.save_screenshot(rutaCompleta)
        driver.quit()

# ---------------------------------------------------------------------------------------------------------------------------