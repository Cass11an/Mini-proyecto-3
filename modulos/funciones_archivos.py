import os
import datetime

def createArchive(bioDriver, dataDriver):
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
        
        FECHA DEL REPORTE: 2025-12-24
        CARRERA: [Nombre de la Ubicación / GP]
        ID DE SESION: [9XXX]
        
        ------------------------------------------------------------
        1. INFORMACION DEL PILOTO
        ------------------------------------------------------------
        
        NOMBRE: [Full Name del Piloto]
        NUMERO: #[Driver Number]
        ESCUDERIA: [Team Name]
        PAIS: [NOMBRE DEL PAIS]
        BIOGRAFIA (Vía Wikipedia):
        [Aquí pegas el primer párrafo extraído con BeautifulSoup]
        
        ------------------------------------------------------------
        2. ESTADISTICAS DE DESEMPEÑO EN CARRERA
        ------------------------------------------------------------
        
        TIEMPO PROMEDIO DE VUELTA: [00:00.000]
        VUELTA MAS RAPIDA: [00:00.000] (Vuelta #X)
        POSICION INICIO CARRERA:
        POSICION FINAL CARRERA: [POSICION FINAL] [VARIACION]
        
        ------------------------------------------------------------
        3. FUENTES Y METADATOS
        ------------------------------------------------------------
        
        - Datos de Telemetria: OpenF1 API (v1)
        - Datos Biograficos: Wikipedia (es.wikipedia.org)
        ============================================================"""
            


    except