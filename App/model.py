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


from DISClib.DataStructures.arraylist import deleteElement, iterator, lastElement
from DISClib.DataStructures.bst import contains
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.ADT import orderedmap as om
import time
assert cf
from datetime import datetime

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
    catalogo["duracion"] = om.newMap(omaptype="RBT",comparefunction=cmpDate)
    catalogo["Horas"] = om.newMap(omaptype="RBT",comparefunction=cmpDate)

    return catalogo

# Funciones para agregar informacion al catalogo
def addAvistamiento (catalogo,avistamiento):
    lt.addLast(catalogo["avistamiento"],avistamiento)
    ciudad = avistamiento["city"]
    Completedate = avistamiento["datetime"]
    duracion = float(avistamiento["duration (seconds)"])
    WhitoutHour = Completedate.split()
    fecha = WhitoutHour[0]
    hour = WhitoutHour[1]
    date = time.strptime(fecha, '%Y-%m-%d')
    finalhour = time.strptime(hour,'%H:%M:%S')
    latCompleta = float(avistamiento["latitude"])
    longCompleta = float(avistamiento["longitude"])
    Latitud = round(latCompleta,2)
    Longitud = round(longCompleta,2)
    UpdateCiudad(catalogo["Ciudad"],avistamiento,ciudad)
    UpdateDates(catalogo["Fechas"],avistamiento,date)
    UpadateLong(catalogo["Longitud"],avistamiento,Longitud,Latitud)
    UpdateSeconds(catalogo["duracion"], avistamiento, duracion, ciudad)
    UpdateHours(catalogo["Horas"], avistamiento, finalhour)
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
    existCity = om.contains(mapa,float(longitud))
    if existCity:
        entry = om.get(mapa,float(longitud))
        valor = me.getValue(entry)
        existlat = om.contains(valor,float(latitud))
        if existlat:
            pareja_lat = om.get(valor,float(latitud))
            valor_lat = me.getValue(pareja_lat)
            lt.addLast(valor_lat,avistamiento)
        else:
            lis2 = lt.newList(datastructure="ARRAY_LIST")
            lt.addLast(lis2,avistamiento)
            om.put(valor,float(latitud),lis2)
    else:
        mapaLat = om.newMap(omaptype="RBT",comparefunction=cmpDate)
        lis = lt.newList(datastructure="ARRAY_LIST")
        lt.addLast(lis,avistamiento)
        om.put(mapaLat,float(latitud),lis)
        om.put(mapa,float(longitud),mapaLat)
def UpdateSeconds (map,avistamiento,duracion, ciudad):
    existCity = om.contains(map,float(duracion))
    if existCity:
        entry = om.get(map,float(duracion))
        valor = me.getValue(entry)
        existlat = om.contains(valor,ciudad)
        if existlat:
            pareja_lat = om.get(valor,ciudad)
            valor_lat = me.getValue(pareja_lat)
            lt.addLast(valor_lat,avistamiento)
        else:
            lis2 = lt.newList(datastructure="ARRAY_LIST")
            lt.addLast(lis2,avistamiento)
            om.put(valor,ciudad,lis2)
    else:
        mapaLat = om.newMap(omaptype="RBT",comparefunction=cmpDate)
        lis = lt.newList(datastructure="ARRAY_LIST")
        lt.addLast(lis,avistamiento)
        om.put(mapaLat,ciudad,lis)
        om.put(map,float(duracion),mapaLat)
def UpdateHours (map,avistamiento,hour):
    existCity = om.contains(map,hour)
    if existCity:
        entry = om.get(map,hour)
        valor = me.getValue(entry)
        lt.addLast(valor,avistamiento)
    else:
        lis = lt.newList(datastructure="ARRAY_LIST")
        lt.addLast(lis,avistamiento)
        om.put(map,hour,lis)
def UpdateHours (map,avistamiento,hour):
    existCity = om.contains(map,hour)
    if existCity:
        entry = om.get(map,hour)
        valor = me.getValue(entry)
        lt.addLast(valor,avistamiento)
    else:
        lis = lt.newList(datastructure="ARRAY_LIST")
        lt.addLast(lis,avistamiento)
        om.put(map,hour,lis)

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
    LongitudesInrange = om.values(mapa,longitudmay,longitudinf)
    iterador1 = lt.iterator(LongitudesInrange)
    i = 1
    while i <= lt.size(LongitudesInrange):
        elemento = next(iterador1)
        LatitudesInRange = om.keys(elemento,latitudinf,latitudmay)
        iterador2 = lt.iterator(LatitudesInRange)
        j = 1 
        while j <= lt.size(LatitudesInRange):
            elemento2 = next(iterador2)
            pareja = om.get(elemento,elemento2)
            valor = me.getValue(pareja)
            if lt.size(valor) > 1:
                recorrerlista(mapa_avistamientos, valor)
            else: 
                latitud = float(lt.getElement(valor,0)["latitude"])
                om.put(mapa_avistamientos,latitud,valor) 
            j +=1
        i+=1
    return mapa_avistamientos

def recorrerlista(mapa_avistamientos, valor):
    iterador3 = lt.iterator(valor)
    i = 1
    while i <= lt.size(valor):
        if i > 1:
            elemento3 = next(iterador3)
            latitud = round(float(elemento3["latitude"]),3)
            om.put(mapa_avistamientos,latitud,valor)
        else:
            elemento3 = next(iterador3)
            latitud = float(elemento3["latitude"])
            om.put(mapa_avistamientos,latitud,valor)
        i+=1 
def AvistamientosBySeconds(mapa, minlimit, maxlimit):
    llaves = om.values(mapa,minlimit,maxlimit)
    elements = lt.iterator(llaves)
    i = 1
    while i <= 3:
        elementos = next(elements)
        elemento = om.minKey(elementos)
        var = om.get(elementos, elemento)
        valor = me.getValue(var)
        if lt.size(valor)> 1:
            z = 0
            while z < lt.size(valor) and i <= 3: 
                info = lt.getElement(valor, z)
                print("-------------------------------")
                print("Date time: " + str(info["datetime"]))
                print("City: " + str(info["city"]))
                print("State: "+ str(info["state"]))
                print("Country: " + str(info["country"]))
                print("Shape: " + str(info["shape"]))
                print("Duration (seconds): " + str(info["duration (seconds)"]))
                elementos = om.deleteMin(elementos)
                z+=1
                i+= 1
        else:
            info = lt.getElement(valor,0)
            print("-------------------------------")
            print("Date time: " + str(info["datetime"]))
            print("City: " + str(info["city"]))
            print("State: "+ str(info["state"]))
            print("Country: " + str(info["country"]))
            print("Shape: " + str(info["shape"]))
            print("Duration (seconds): " + str(info["duration (seconds)"]))

        i+=1
    j = 0
    while j <=2:
        elementos = lt.getElement(llaves, lt.size(llaves) - j)
        elemento = om.minKey(elementos)
        var = om.get(elementos, elemento)
        valor = me.getValue(var)
        if lt.size(valor)> 1:
            m = 0
            while m < lt.size(valor) and j <= 3: 
                info = lt.getElement(valor, m)
                print("-------------------------------")
                print("Date time: " + str(info["datetime"]))
                print("City: " + str(info["city"]))
                print("State: "+ str(info["state"]))
                print("Country: " + str(info["country"]))
                print("Shape: " + str(info["shape"]))
                print("Duration (seconds): " + str(info["duration (seconds)"]))
                elementos = om.deleteMin(elementos)
                m+=1
                j+= 1
        else:
            info = lt.getElement(valor,0)
            print("-------------------------------")
            print("Date time: " + str(info["datetime"]))
            print("City: " + str(info["city"]))
            print("State: "+ str(info["state"]))
            print("Country: " + str(info["country"]))
            print("Shape: " + str(info["shape"]))
            print("Duration (seconds): " + str(info["duration (seconds)"]))

        j+=1


    
def HoursInRange(mapa,hour1,hour2):
    llaves = om.values(mapa,hour1,hour2)
    iter1 = lt.iterator(llaves)
    i = 1 
    while i <= 3:
        elementos = next(iter1)
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
