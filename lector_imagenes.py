#Convertidor de imagenes a texto

#simplemente archivos que debemos importar
from PIL import Image
from pytesseract import *

# Ubicamos la ruta de Tesseract, esta direccion es de la instalación inicial de teseract
pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# La imagen en tu carpeta
imagen = Image.open("foto-esp.png")

# Procesamos la imagen para extraer el texto, convierte la imagen a texto
# Para que lea en ingles la imagen debe estar en ingles y debemos quitar el lang='spa'

resultado = pytesseract.image_to_string(imagen, lang='spa')

print(resultado)
 