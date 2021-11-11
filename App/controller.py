"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de avistamientos
def initCatalog():
    catalogo = model.newCatalog()
    return catalogo

# Funciones para la carga de datos
def loadData(catalogo, Ufofile):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    UFoFile = cf.data_dir + Ufofile
    input_file = csv.DictReader(open(UFoFile, encoding="utf-8"),
                                delimiter=",")
    for avistamiento in input_file:
        model.addAvistamiento(catalogo, avistamiento)
    return catalogo

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
def AvistamientosByCity(catalog,ciudad):
    mapa = catalog["Ciudad"]
    return model.AvistamientosByCity(mapa,ciudad)
def DatesInRange(catalog,fecha1,fecha2):
    mapa = catalog["Fechas"]
    model.DatesInRange(mapa,fecha1,fecha2)
def AvistamientosInRange(catalogo,longitudinf,longitudmay,latitudinf,latitudmay):
    mapa = catalogo["Longitud"]
    return model.AvistamientosInRange(mapa,longitudinf,longitudmay,latitudinf,latitudmay)
def AvistamientosBySeconds(catalog, minlimit, maxlimit):
    mapa = catalog["duracion"]
    return model.AvistamientosBySeconds(mapa, minlimit, maxlimit)   
def HoursInRange(catalog,hora1,hora2):
    mapa = catalog["Horas"]
    model.HoursInRange(mapa,hora1,hora2)

def indexHeight(mapa):
 
    return model.indexHeight(mapa)


def indexSize(mapa):

    return model.indexSize(mapa)
