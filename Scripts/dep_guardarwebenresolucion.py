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
from selenium.webdriver import Chrome


class GuardarWebEnResolucion():
    
    """ **************************************************************** 
    Clase creada para guardar una captura de pantalla, de una url, a una
    determinada resolución.

    Contiene las variables de instancia url, de tipo str, y resolución,
    instancia de la clase Resolucion()
    *************************************************************** """

    # Constructor
    def __init__(self, url = '', resolucion = Resolucion(320, 568, 'No especificado', 'No especificado')):
        self.url = url
        self.resolucion = resolucion
        self.run()
    
    def run(self):
        nombreImagen = "{0}x{1}_{2}_{3}".format(self.resolucion.ancho, self.resolucion.alto, self.resolucion.tipo, self.resolucion.nombre)
        driver = Chrome()
        driver.set_window_size(self.resolucion.ancho, self.resolucion.alto)
        driver.get(self.url)
        driver.save_screenshot("Screenshot/{0}.png".format(nombreImagen))
        driver.quit()


# ---------------------------------------------------------------------------------------------------------------------------

# Temporal, desaparecerá de la versión inicial, solo para probar la clase.
if __name__ == '__main__':
    guardarWebEnResolucion = GuardarWebEnResolucion('https://www.ortizsanchezdev.es', Resolucion(1024,768,"qa1","qa1"))