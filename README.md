# Desarrollo de Herramientas de Red - Python

Repositorio dedicado a la implementación de herramientas de red y seguridad utilizando Python. El enfoque principal de este proyecto es el manejo de conexiones a bajo nivel y la comprensión de protocolos de transporte.

## Descripción del Proyecto

El código incluido permite realizar escaneos de puertos sobre direcciones IP específicas para identificar servicios activos. Se prioriza la eficiencia en la gestión de conexiones y el manejo de excepciones de red.

### Características Técnicas
* **Protocolos:** Implementación sobre TCP mediante el uso de la librería estándar `socket`.
* **Validación:** Identificación de puertos mediante el análisis de códigos de error de conexión (`connect_ex`).
* **Entorno:** Desarrollado y testeado en sistemas Linux.

## Estructura del Código

1.  **Creación de Sockets:** Configuración de sockets IPv4 y flujo de datos TCP.
2.  **Gestión de Timeouts:** Control de tiempos de espera para optimizar la velocidad del escaneo en redes con latencia.
3.  **Captura de Banners:** Intento de recepción de datos para la identificación preliminar de servicios en puertos abiertos.

## Instrucciones de Uso

Para ejecutar las herramientas en un entorno local:

```bash
# Clonar el repositorio
git clone https://github.com/cableOTA-png/escanerv0.git

# Ejecutar el script principal
python3 scanner.py
