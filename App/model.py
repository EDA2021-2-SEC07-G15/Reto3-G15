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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


from DISClib.DataStructures.arraylist import deleteElement, lastElement
from DISClib.DataStructures.bst import contains
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.ADT import orderedmap as om
import time
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    catalogo = {"avistamiento" : None,
                "Ciudad" : None}
    catalogo["avistamiento"] = lt.newList(datastructure="ARRAY_LIST")
    catalogo["Ciudad"] = mp.newMap(1000,maptype="CHAINING", loadfactor=0.5)
    catalogo["Fechas"] = om.newMap(omaptype="RBT",comparefunction=cmpDate)
    catalogo["Longitud"] = om.newMap(omaptype="RBT",comparefunction=cmpDate)
    return catalogo

# Funciones para agregar informacion al catalogo
def addAvistamiento (catalogo,avistamiento):
    lt.addLast(catalogo["avistamiento"],avistamiento)
    ciudad = avistamiento["city"]
    Completedate = avistamiento["datetime"]
    WhitoutHour = Completedate.split()
    fecha = WhitoutHour[0]
    date = time.strptime(fecha, '%Y-%m-%d')
    latCompleta = float(avistamiento["latitude"])
    longCompleta = float(avistamiento["longitude"])
    Latitud = round(latCompleta,2)
    Longitud = round(longCompleta,2)
    UpdateCiudad(catalogo["Ciudad"],avistamiento,ciudad)
    UpdateDates(catalogo["Fechas"],avistamiento,date)
    UpadateLong(catalogo["Longitud"],avistamiento,Longitud,Latitud)
    return catalogo
def UpdateCiudad(map,avistamiento,city):
    existCity = mp.contains(map,city)
    if existCity:
        entry = mp.get(map,city)
        valor = me.getValue(entry)
        lt.addLast(valor,avistamiento)
    else:
        lis = lt.newList(datastructure="ARRAY_LIST")
        lt.addLast(lis,avistamiento)
        mp.put(map,city,lis)
def UpdateDates (map,avistamiento,fecha):
    existCity = om.contains(map,fecha)
    if existCity:
        entry = om.get(map,fecha)
        valor = me.getValue(entry)
        lt.addLast(valor,avistamiento)
    else:
        lis = lt.newList(datastructure="ARRAY_LIST")
        lt.addLast(lis,avistamiento)
        om.put(map,fecha,lis)
def UpadateLong(mapa,avistamiento,longitud,latitud):
    existCity = om.contains(mapa,longitud)
    if existCity:
        entry = om.get(mapa,longitud)
        valor = me.getValue(entry)
        om.put(valor,latitud,avistamiento)
        print("hola")
        
    else:
        mapaLat = om.newMap(omaptype="RBT",comparefunction=cmpDate)
        om.put(mapaLat,latitud,avistamiento)
        om.put(mapa,longitud,mapaLat)

# Funciones para creacion de datos

# Funciones de consulta
def AvistamientosByCity(mapa,city):
    entry = mp.get(mapa,city)
    AvistamientosCity = om.newMap(omaptype="RBT",comparefunction=cmpDate)
    if entry != None:
        avistamientosBycity = me.getValue(entry)
        i = 1
        while i <= lt.size(avistamientosBycity):
            avistamiento = lt.getElement(avistamientosBycity,i)
            fecha = avistamiento["datetime"]
            fechaAcomparar = time.strptime(fecha, '%Y-%m-%d %H:%M:%S')
            existCity = om.contains(AvistamientosCity,fechaAcomparar)
            if existCity:
                pareja = om.get(AvistamientosCity,fechaAcomparar)
                valor = me.getValue(pareja)
                lt.addLast(valor,avistamiento)
            else:
                om.put(AvistamientosCity,fechaAcomparar,avistamiento)

            i += 1 
    return AvistamientosCity
def DatesInRange(mapa,fecha1,fecha2):
    llaves = om.values(mapa,fecha1,fecha2)
    elements = lt.iterator(llaves)
    i = 1 
    while i <= 3:
        elementos = next(elements)
        elemento = lt.getElement(elementos,0)
        print("-----------------------")
        print("Date time: " + str(elemento["datetime"]))
        print("City: " + str(elemento["city"]))
        print("State: "+ str(elemento["state"]))
        print("Country: " + str(elemento["country"]))
        print("Shape: " + str(elemento["shape"]))
        print("Duration (seconds): " + str(elemento["duration (seconds)"]))
        i +=1
    j = 1
    while j <= 3:
        elementos = lt.removeLast(llaves)
        elemento = lt.getElement(elementos,0)
        print("-----------------------")
        print("Date time: " + str(elemento["datetime"]))
        print("City: " + str(elemento["city"]))
        print("State: "+ str(elemento["state"]))
        print("Country: " + str(elemento["country"]))
        print("Shape: " + str(elemento["shape"]))
        print("Duration (seconds): " + str(elemento["duration (seconds)"]))
        j += 1
def AvistamientosInRange(mapa,longitudinf,longitudmay,latitudinf,latitudmay):
    mapa_avistamientos = om.newMap(omaptype="RBT",comparefunction=cmpDate)
    LongitudesInrange = om.values(mapa,longitudinf,longitudmay)
    iterador1 = lt.iterator(LongitudesInrange)
    i = 1
    while i <= lt.size(LongitudesInrange):
        elemento = next(iterador1)
        LatitudesInRange = om.values(elemento,latitudinf,latitudmay)
        iterador2 = lt.iterator(LatitudesInRange)
        j = 1 
        while j <= lt.size(LatitudesInRange):
            elemento2 = next(iterador2)
            latitud = elemento2["latitude"]
            om.put(mapa_avistamientos,latitud,elemento2)
            j +=1
        i+=1
    return mapa_avistamientos



def indexHeight(mapa):

    return om.height(mapa)


def indexSize(mapa):

    return om.size(mapa)


# Funciones utilizadas para comparar elementos dentro de una lista
def cmpDate(date1,date2):
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1

# Funciones de ordenamiento
