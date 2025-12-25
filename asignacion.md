# Punto de Parada 3: El Agente de Información (Web & OS)

Nuevos temas agregados: APIs REST, Web Scraping, Scripts del Sistema Operativo (os, shutil).

### 🕵️ Proyecto Retador 3: "El Investigador Digital Autónomo"

**Duración:** 3 días.

Descripción:

Una herramienta que investiga un tema, descarga evidencia y organiza su propio espacio de trabajo en la computadora.

**Requerimientos Técnicos:**

1. **Consumo de API:** Conectarse a una API pública (ej: OpenWeather o una de noticias/criptomonedas) para obtener datos en tiempo real (JSON) y extraer lo importante y guardarlos para ser mostrados. **listo**
2. **Web Scraping:** Entrar a una página web (ej: Wikipedia o un blog), extraer el título principal (`h1`) y el primer párrafo de introducción usando `BeautifulSoup o Playwright` y guardarlo para ser mostrado. **listo**
3. **Reporte Unificado:** Crear un archivo `investigacion_hoy.txt` que combine los datos de la API y el texto del Scraping. **listo**
4. **Organización del Sistema Operativo (OS/Shutil):**
    - Al finalizar, el script debe revisar su propia carpeta.
    - Si hay reportes viejos, debe moverlos a una carpeta llamada `/Historial/[Año-Mes]`. Reportes ademas del de hoy, se organizan en sus respectivas carpetas
    - Debe eliminar archivos temporales si se crearon.
5. **Interfaz de Usuario:** Todo debe correrse desde consola y tener un menu para eligir que reporte mostrar.



