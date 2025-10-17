import pyqrcode
# Cadena de la que queremos generar el QR
s = "https://www.colegiovivas.com"
# Generación
url = pyqrcode.create(s)
# Se guarda como png
url.png("myqr.png", scale=6)

# oiste, si no tienes pip installa la opcion de version 3.14 de python y modifica las opciomes de instalacio como pone en los apuntes al principioo valee ahora veo
