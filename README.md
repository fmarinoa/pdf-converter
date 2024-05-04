# PDF Converter & Merger

Este proyecto es una aplicación de escritorio simple que te permite convertir imágenes (en formatos PNG, JPG, etc.) en archivos PDF. También puedes combinar varios archivos PDF en uno solo.

## Features

- Convierte archivos PNG, JPG y JPEG a PDF.
- Une varios archivos de tipo PDF en uno.
- Permite al usuario seleccionar el orden de los archivos antes de la conversión o la unión.

## Requirements

- Python 3.x
- Pillow
- pypdf
- reportlab

## Convertir la aplicación en un ejecutable
Si deseas compartir tu aplicación con otras personas y permitirles ejecutarla fácilmente en sus máquinas sin necesidad de instalar Python u otras dependencias, puedes convertirla en un ejecutable. Aquí te muestro cómo hacerlo en Windows 10 usando PyInstaller:

- Instala PyInstaller: Si aún no tienes PyInstaller instalado, puedes hacerlo con el siguiente comando:
- pip install pyinstaller
- Navega al directorio del proyecto: Abre una terminal y navega hasta el directorio que contiene tu archivo main.py y otros archivos necesarios para tu aplicación.
Crea el ejecutable: Ejecuta el siguiente comando para crear el ejecutable:
- pyinstaller --noconsole --onefile main.py
- Esto creará un directorio dist en tu proyecto, y dentro de este directorio encontrarás tu ejecutable. El argumento --onefile indica a PyInstaller que cree un solo archivo ejecutable en lugar de un conjunto de archivos.
- Distribuye el ejecutable: Ahora puedes compartir el archivo ejecutable (main.exe) que se encuentra en el directorio dist con otras personas. Pueden ejecutar este archivo en sus máquinas sin necesidad de tener Python instalado.
