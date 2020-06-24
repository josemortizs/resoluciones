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
from gestorresoluciones import GestorResoluciones
from guardarwebenresolucion import GuardarWebEnResolucion
from resolucion import Resolucion


class GuardaResoluciones():

    """ **************************************************************** 
    Clase que recibe una URL, como parámetro al instanciar un objeto de
    la misma, y almacena una captura de pantalla de dicha URL, en el 
    navegador Chrome, en distintas resoluciones.

    Las distintas resoluciones están almacenadas en el fichero:
    Data/DatosGestorResoluciones.csv
    Las capturas de pantalla se almacenan en la carpeta:
    /Screenshot/
    *************************************************************** """ 

    # Constructor
    def __init__(self, url = ''):
        self.url = url
        self.gestorresoluciones = GestorResoluciones()
        self.run()
    

    def run(self):
        for resolucion in self.gestorresoluciones.resoluciones:
            guardarwebenresolucion = GuardarWebEnResolucion(self.url, resolucion)
            guardarwebenresolucion.start()


    
# ---------------------------------------------------------------------------------------------------------------------------

# Temporal, desaparecerá de la versión inicial, solo para probar la clase.
if __name__ == '__main__':
   resoluciones = GuardaResoluciones('https://www.ortizsanchezdev.es')