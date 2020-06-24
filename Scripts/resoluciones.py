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
from guardaresoluciones import GuardaResoluciones
import sys

try:
    URL = sys.argv[1]
except IndexError as ex:
    print(
        "\nHa de aportar, como argumento, una dirección URL, ejemplo de uso: \n   python3 resoluciones.py https://www.ortizsanchezdev.es \n",
        file=sys.stderr
    )
    sys.exit()

print("url: " ,URL)

guardaresoluciones = GuardaResoluciones('www.google.com')
