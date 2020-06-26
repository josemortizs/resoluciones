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

from resolucion import Resolucion
from gestorresoluciones import GestorResoluciones

def guardaResolucionesIniciales():

    gestorresoluciones = GestorResoluciones()

    gestorresoluciones.agregaResolucion(Resolucion(1920,1080,'PC','Full HD'))
    gestorresoluciones.agregaResolucion(Resolucion(1366,768,'PC','HD'))
    gestorresoluciones.agregaResolucion(Resolucion(1024,768,'PC','XVGA'))
    gestorresoluciones.agregaResolucion(Resolucion(1280,1024,'PC','SXGA'))

    gestorresoluciones.imprimeListadoResoluciones()

# -------------------------------------------------------------------------------------------------------------------- #

# Temporal, desaparecerá de la versión inicial, solo para probar la clase.
if __name__ == '__main__':
    guardaResolucionesIniciales()