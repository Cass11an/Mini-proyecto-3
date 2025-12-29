import os
from datetime import datetime
import time
import shutil
import re

#FUNCIONES PARA GENERAR ARCHIVOS DE REPORTE

fecha = datetime.now()
fechaFormato = fecha.strftime('%d-%m-%Y')

def createArchive(dataDriver):
    

    try:
        ubicacionActual = os.path.dirname(os.path.abspath(__file__)) #busca la uubicacion del archivo main.py
        ubicacionReportes = os.path.join(ubicacionActual, "..", "reportes") #busca la carpeta de reportes y crea la nueva ubicacion

        if not os.path.exists(ubicacionReportes):
            os.makedirs(ubicacionReportes)
        
        nombreArchivo = f'reporte_{dataDriver['searchName']}_' + fechaFormato + '.txt'
        ubicacionArchivo = os.path.join(ubicacionReportes, nombreArchivo)

        content = f"""        ============================================================
        REPORTE DE INVESTIGACION - FORMULA 1 (Temporada 2025)
        ============================================================
        
        FECHA DEL REPORTE: {fechaFormato}
        CARRERA: {dataDriver['nameSession']}
        ID DE SESION: {dataDriver['IDsession']}
        
        ------------------------------------------------------------
        1. INFORMACION DEL PILOTO
        ------------------------------------------------------------
        
        NOMBRE: {dataDriver['fullName']}
        ESCUDERIA: {dataDriver['teamName']}
        PAIS: {dataDriver['country']}
        BIOGRAFIA (Vía Wikipedia):
        {dataDriver['title']}
        {dataDriver['biography']}
        
        ------------------------------------------------------------
        2. ESTADISTICAS DE DESEMPEÑO EN CARRERA
        ------------------------------------------------------------
        
        TIEMPO PROMEDIO DE VUELTA: {dataDriver['promLap']: .3f}
        VUELTA MAS RAPIDA: {dataDriver['bestLap']}
        POSICION INICIO CARRERA: {dataDriver['start']}
        POSICION FINAL CARRERA: {dataDriver['end']} ({dataDriver['change']})
        
        ------------------------------------------------------------
        3. FUENTES Y METADATOS
        ------------------------------------------------------------
        
        - Datos de Telemetria: OpenF1 API (v1)
        - Datos Biograficos: Wikipedia (es.wikipedia.org)
        ============================================================"""

        document = open(f'{ubicacionArchivo}', "w", encoding="utf-8")
        document.write(content)
        document.close()

        print(f'Se ha generado el archivo: {nombreArchivo}!. Revisa la carpeta **reportes** ') 

    except Exception as e:
        print(f'Ha ocurrido un error al generar el reporte: {e}')

#FUNCIONES PARA GESTION DE CARPETAS

def order_historial_folder():

    ubicacionActual = os.path.dirname(os.path.abspath(__file__))
    ubicacionHistorial = os.path.join(ubicacionActual,'..', 'reportes\\historial')

    #extraemos los nombres de las carpetas de acuerdo a la fecha de los archivos
    for file in os.listdir(ubicacionHistorial):

        if file.endswith('.txt'):
            ubicacionArchivo = os.path.join(ubicacionHistorial, file)
            substr = re.search(r'\d{2}[-]\d{2}[-]\d{4}', file)
            dateFile = datetime.strptime(substr.group(), '%d-%m-%Y')
            nameFolder = '[' + dateFile.strftime('%B-%Y') + ']'

            pathFolder = os.path.join(ubicacionHistorial, nameFolder)
            if not os.path.exists(pathFolder):
                os.mkdir(pathFolder)
            shutil.move(ubicacionArchivo, pathFolder)

def order_folder():

    ubicacionActual = os.path.dirname(os.path.abspath(__file__))
    ubicacionReportes = os.path.join(ubicacionActual,'..', 'reportes')

    historial = os.path.join(ubicacionReportes, 'historial')
    if not os.path.exists(historial):
        os.mkdir(historial)
    
    for file in os.listdir(ubicacionReportes):
        if fechaFormato not in file and file != 'historial':
            origin = os.path.join(ubicacionReportes, file)
            shutil.move(origin, historial)
    order_historial_folder()
    print('Se han ordenado los reportes.')

def clean_temp_files():
    ubicacionActual = os.path.dirname(os.path.abspath(__file__))
    ubicacionTemp = os.path.join(ubicacionActual,'..', 'modulos\\__pycache__')

    try:
        if os.path.isfile(ubicacionTemp): #si es solo un archivo
            os.remove(ubicacionTemp)
        elif os.path.isdir(ubicacionTemp): #si es un directorio
            shutil.rmtree(ubicacionTemp)
        
        print('Se han eliminado los archivos temporales')
    except Exception as e:
        print(f"Error al eliminar el archivo: {e}")   

def create_URL(numberDriver, searchName):
    generalURL = 'https://es.wikipedia.org/wiki/'

    match numberDriver:
        case 63: URL = generalURL + 'George_Russell_(piloto)'
        case 55: URL = generalURL + 'Carlos_Sainz_Jr.'
        case _: URL = generalURL + searchName

    return URL

def safe_update(dataDriver, function):
    if function:
        dataDriver.update(function)
    else:
        print(f'No se ha podido obtener la informacion de: {function}')

def show_menu():
    time.sleep(5)
    os.system('cls||clear')

    menu = """
    ============================================================
            SISTEMA DE MONITOREO Y REPORTE DE FÓRMULA 1 
            Investigador Digital Autónomo - Temporada 2025
    ============================================================
    Este programa automatiza la recopilación de datos de la API
    de F1 y Wikipedia para generar reportes detallados sobre el
    desempeño del piloto a elegir.

    1. GENERAR REPORTE: Extrae estadísticas del piloto seleccionado.
    2. ORDENAR: Clasifica archivos en carpetas por Mes-Año.
    3. LIMPIAR: Borra archivos temporales del sistema.
    0. SALIR

    Seleccione una opción: """

    return input(menu)


