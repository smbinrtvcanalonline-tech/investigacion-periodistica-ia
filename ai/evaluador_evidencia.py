# ==================================================
# EVALUADOR DE EVIDENCIA DOCUMENTAL
# Investigación Periodística IA
# SMBINRTV
# ==================================================


def evaluar_evidencia(documento):

    resultado = {

        "tipo": "",
        "nivel_confianza": "",
        "observacion": ""

    }


    if documento:

        resultado["tipo"] = "Documento recibido"

        resultado["nivel_confianza"] = (
            "Requiere verificación"
        )

        resultado["observacion"] = (
            "La información debe contrastarse "
            "con fuentes oficiales."
        )

    else:

        resultado["tipo"] = "Sin evidencia"

        resultado["nivel_confianza"] = (
            "No determinado"
        )

        resultado["observacion"] = (
            "No existen documentos para analizar."
        )


    return resultado



if __name__ == "__main__":

    prueba = evaluar_evidencia(
        "Expediente público"
    )

    print(prueba)
