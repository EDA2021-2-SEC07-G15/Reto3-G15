"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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

import time
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from datetime import datetime


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
Ufofile = "UFOS-utf8-small.csv"
def printMenu():
    print("---------------------------------------")
    print("\n")
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Cargar avistamientos")
    print("3- Contar avistamientos en una ciudad")
    print("4- Contar avistamientos por duracion")
    print("5- Contar avistamientos por hora/minutos del dia")
    print("6- Contar avistamientos en un rango de fechas")
    print("7- Contar avistamientos de una zona geográfica")
    print("\n")
    print("---------------------------------------")
def PrintResults1(mapa,ciudad):
    cantidadAv = om.size(mapa)
    print("Hay " + str(cantidadAv) + " avistamientos en: " + str(ciudad))
    print("Los primeros y ultimos 3 son: ")
    rango = 3
    mapaArecorrer = mapa 
    i = 1
    while i <= rango:
        llave = om.minKey(mapaArecorrer)
        pareja = om.get(mapaArecorrer,llave)
        valor = me.getValue(pareja)
        print("-------------------------------")
        print("Date time: " + str(valor["datetime"]))
        print("City: " + str(ciudad))
        print("State: "+ str(valor["state"]))
        print("Country: " + str(valor["country"]))
        print("Shape: " + str(valor["shape"]))
        print("Duration (seconds): " + str(valor["duration (seconds)"]))
        mapaArecorrer = om.deleteMin(mapaArecorrer)
        i+=1
    j = 1 
    while j <= rango and om.size(mapaArecorrer) >= 1:
        llave = om.maxKey(mapaArecorrer)
        pareja = om.get(mapaArecorrer,llave)
        valor = me.getValue(pareja)
        print("-------------------------------")
        print("Date time: " + str(valor["datetime"]))
        print("City: " + str(ciudad))
        print("State: "+ str(valor["state"]))
        print("Country: " + str(valor["country"]))
        print("Shape: " + str(valor["shape"]))
        print("Duration (seconds): " + str(valor["duration (seconds)"]))
        mapaArecorrer = om.deleteMax(mapaArecorrer)
        j +=1 
def PrintResults5(mapa):
    print("There are " + str(om.size(mapa)) + " different UFO sightings in the current area")
    print("The first 5 and last 5 UFO sightings in this time are: ")
    mapaArecorrer = mapa
    if om.size(mapa) >= 10:
        rango = 5
        i = 1
        while i <= rango:
            llave = om.minKey(mapaArecorrer)
            pareja = om.get(mapaArecorrer,llave)
            elemento = me.getValue(pareja)
            valor = lt.getElement(elemento,0)
            print("-------------------------------")
            print("Date time: " + str(valor["datetime"]))
            print("City: " + str(valor["city"]))
            print("State: "+ str(valor["state"]))
            print("Country: " + str(valor["country"]))
            print("Shape: " + str(valor["shape"]))
            print("Duration (seconds): " + str(valor["duration (seconds)"]))
            print("latitude: " + str(valor["latitude"]))
            print("longitude: " + str(valor["longitude"]))
            mapaArecorrer = om.deleteMin(mapaArecorrer)
            i+=1
        j = 1 
        while j <= rango and om.size(mapaArecorrer) >= 1:
            llave = om.maxKey(mapaArecorrer)
            pareja = om.get(mapaArecorrer,llave)
            elemento = me.getValue(pareja)
            valor = lt.getElement(elemento,0)
            print("-------------------------------")
            print("Date time: " + str(valor["datetime"]))
            print("City: " + str(valor["city"]))
            print("State: "+ str(valor["state"]))
            print("Country: " + str(valor["country"]))
            print("Shape: " + str(valor["shape"]))
            print("Duration (seconds): " + str(valor["duration (seconds)"]))
            print("latitude: " + str(valor["latitude"]))
            print("longitude: " + str(valor["longitude"]))
            mapaArecorrer = om.deleteMax(mapaArecorrer)
            j +=1 
    else:
        rango = om.size(mapa)
        i = 1
        while i <= rango:
            llave = om.minKey(mapaArecorrer)
            pareja = om.get(mapaArecorrer,llave)
            elemento = me.getValue(pareja)
            valor = lt.getElement(elemento,0)
            print("-------------------------------")
            print("Date time: " + str(valor["datetime"]))
            print("City: " + str(valor["city"]))
            print("State: "+ str(valor["state"]))
            print("Country: " + str(valor["country"]))
            print("Shape: " + str(valor["shape"]))
            print("Duration (seconds): " + str(valor["duration (seconds)"]))
            print("latitude: " + str(valor["latitude"]))
            print("longitude: " + str(valor["longitude"]))

            mapaArecorrer = om.deleteMin(mapaArecorrer)
            i+=1




catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = controller.initCatalog()
    elif int(inputs[0]) == 2:
        print("Cargando información de los avistamientos... ")
        controller.loadData(catalog,'UFOS-utf8-small.csv')
        print("Se han cargado los datos exitosamente")
        print("Total de datos cargados: " + str(lt.size(catalog["avistamiento"])))
    elif int(inputs[0]) == 3:
        ciudad = input("Ingrese la ciudad que desea consultar: ")
        mapa_de_ciudad = controller.AvistamientosByCity(catalog,ciudad)
        print('Altura del arbol: ' + str(controller.indexHeight(mapa_de_ciudad)))
        print('Elementos en el arbol: ' + str(controller.indexSize(mapa_de_ciudad)))
        PrintResults1(mapa_de_ciudad,ciudad)
    elif int(inputs[0]) == 4:
        maxlimit = float (input ("Ingrese la duración máxima en segundos: "))
        minlimit = float (input ("Ingrese la duración mínima en segundos: "))
        mapaAvistamientosPorRangoDeSegundos = controller.AvistamientosBySeconds(catalog, minlimit, maxlimit)   
    elif int(inputs[0]) == 5:
        minlimit = input ("Ingrese la hora mínima en formato HH:MM:SS: ")
        minLimit1 = time.strptime(minlimit,'%H:%M:%S')
        maxlimit = input ("Ingrese la hora máxima en formato HH:MM:SS: ")
        maxlimit1 = time.strptime(maxlimit,'%H:%M:%S')
        mapaAvistamientosPorHoraMinutos = controller.HoursInRange(catalog, minLimit1, maxlimit1) 
    elif int(inputs[0]) == 6:
        print("Hay " + str(om.size(catalog["Fechas"])) + " avistamientos de UFO en diferentes fechas [YYYY-MM-DD]")
        print("El avistamiento más antiguo es: ")
        Oldest = om.minKey(catalog["Fechas"])
        pareja = om.get(catalog["Fechas"], Oldest)
        valor = me.getValue(pareja)
        tamaño = lt.size(valor)
        print("Date: " + str(Oldest) + "count: " + str(tamaño))
        fecha1 = input("Ingrese la primera fecha en formato (YYYY-MM-DD): ")
        date1 = time.strptime(fecha1, '%Y-%m-%d')
        fecha2 = input("Ingrese la segunda fecha en formato (YYYY-MM-DD): ")
        date2 = time.strptime(fecha2, '%Y-%m-%d')
        llaves = controller.DatesInRange(catalog,date1,date2)
    elif int(inputs[0]) == 7:
        Longitud_inf = float(input("Ingrese el limite inferior de longitud: "))
        Longitud_May = float(input("Ingrese el limite superior de longitud: "))
        Latitud_inf = float(input("Ingrese el limite inferior de latitud: "))
        Latitud_May = float(input("Ingrese el limite superior de latitud: "))
        mapa = controller.AvistamientosInRange(catalog,Longitud_inf,Longitud_May,Latitud_inf,Latitud_May)
        PrintResults5(mapa)
    else:
        sys.exit(0)
sys.exit(0)
