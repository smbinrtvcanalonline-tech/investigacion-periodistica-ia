# ==================================================
# CARGADOR DE DOCUMENTOS
# Investigación Periodística IA
# SMBINRTV
# ==================================================

import os


def validar_documento(ruta):

    resultado = {
        "archivo": ruta,
        "existe": False,
        "tipo": ""
    }


    if os.path.exists(ruta):

        resultado["existe"] = True

        extension = os.path.splitext(ruta)[1]

        resultado["tipo"] = extension


    return resultado



def obtener_tipo_documento(ruta):

    extension = os.path.splitext(ruta)[1]

    tipos = {

        ".pdf": "Documento PDF",
        ".docx": "Documento Word",
        ".xlsx": "Archivo Excel",
        ".jpg": "Imagen",
        ".png": "Imagen"

    }


    return tipos.get(
        extension,
        "Formato no identificado"
    )



if __name__ == "__main__":

    prueba = validar_documento(
        "expediente.pdf"
    )

    print(prueba)
