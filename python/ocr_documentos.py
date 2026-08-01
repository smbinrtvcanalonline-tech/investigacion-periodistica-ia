# ==================================================
# OCR PARA DOCUMENTOS
# Investigación Periodística IA
# SMBINRTV
# ==================================================


def extraer_texto_imagen(archivo):

    resultado = {

        "archivo": archivo,

        "texto_extraido": "",

        "estado": ""

    }


    if archivo:

        resultado["estado"] = (
            "Documento enviado a OCR"
        )

        resultado["texto_extraido"] = (
            "Texto pendiente de procesamiento OCR"
        )


    else:

        resultado["estado"] = (
            "No existe archivo"
        )


    return resultado



if __name__ == "__main__":

    prueba = extraer_texto_imagen(
        "documento.jpg"
    )

    print(prueba)
