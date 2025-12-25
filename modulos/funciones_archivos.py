import os
import datetime

dataDriver = {
            'start': "start",
            'end': "end",
            'change': "change",
            'bestLap': "bestLap",
            'promLap': "promLap",
            "teamName": "team_name",
            "country": "country_code",
            "fullName": "full_name",
            'searchName': "shearchName",
            'title': "title",
            'biography': "biography"
            }

def createArchive(dataDriver):
    fecha = datetime.now()
    fechaFormato = fecha.strftime('%d/%m/%Y')

    try:
        ubicacionActual = os.path.dirname(os.path.abspath(__file__)) #busca la uubicacion del archivo main.py
        ubicacionReportes = os.path.join(ubicacionActual, "..", "reportes") #busca la carpeta de reportes y crea la nueva ubicacion

        if not os.path.exists(ubicacionReportes):
            os.makedirs(ubicacionReportes)
        
        nombreArchivo = 'reporte' + fechaFormato + '.txt'
        ubicacionArchivo = os.path.join(ubicacionReportes, nombreArchivo)

        content = F"""============================================================
        REPORTE DE INVESTIGACION - FORMULA 1 (Temporada 2025)
        ============================================================
        
        FECHA DEL REPORTE: {fechaFormato}
        CARRERA: [Nombre de la Ubicación / GP]
        ID DE SESION: [9XXX]
        
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
        
        TIEMPO PROMEDIO DE VUELTA: {dataDriver['title']}
        VUELTA MAS RAPIDA: {dataDriver['title']}
        POSICION INICIO CARRERA: {dataDriver['title']}
        POSICION FINAL CARRERA: {dataDriver['title']} ({dataDriver['title']})
        
        ------------------------------------------------------------
        3. FUENTES Y METADATOS
        ------------------------------------------------------------
        
        - Datos de Telemetria: OpenF1 API (v1)
        - Datos Biograficos: Wikipedia (es.wikipedia.org)
        ============================================================"""


            


    except