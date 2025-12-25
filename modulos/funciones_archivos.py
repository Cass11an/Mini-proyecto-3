import os
from datetime import datetime
import shutil

fecha = datetime.now()
fechaFormato = fecha.strftime('%d-%m-%Y')

def createArchive(dataDriver):
    

    try:
        ubicacionActual = os.path.dirname(os.path.abspath(__file__)) #busca la uubicacion del archivo main.py
        ubicacionReportes = os.path.join(ubicacionActual, "..", "reportes") #busca la carpeta de reportes y crea la nueva ubicacion

        if not os.path.exists(ubicacionReportes):
            os.makedirs(ubicacionReportes)
        
        nombreArchivo = 'reporte_' + fechaFormato + '.txt'
        ubicacionArchivo = os.path.join(ubicacionReportes, nombreArchivo)

        content = f"""============================================================
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
        
        TIEMPO PROMEDIO DE VUELTA: {dataDriver['promLap']}
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

        print(f'Se ha generado el reporte {nombreArchivo}')          

    except Exception as e:
        print(f'Ha ocurrido un error al generar el reporte: {e}')


def order_folder():

    ubicacionActual = os.path.dirname(os.path.abspath(__file__))
    ubicacionReportes = os.path.join(ubicacionActual,'..', 'reportes')

    historial = os.path.join(ubicacionReportes, 'historial')
    if not os.path.exists(historial):
        os.mkdir(historial)

    for file in os.listdir(ubicacionReportes):
        if file != f"reporte_{fechaFormato}.txt":
            origin = os.path.join(ubicacionReportes, file)
            shutil.move(origin, historial)