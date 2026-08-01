# ==================================================
# CONTROL DE CALIDAD PERIODÍSTICO IA
# SMBINRTV - TÚ DECIDES
# ==================================================


def revisar_informe(informe):

    resultado = {

        "estado": "Revisión realizada",

        "alertas": [],

        "recomendaciones": []

    }


    if not informe:

        resultado["alertas"].append(
            "El informe está vacío"
        )

        return resultado



    resultado["recomendaciones"].append(
        "Verificar todas las fuentes citadas"
    )


    resultado["recomendaciones"].append(
        "Separar hechos comprobados de hipótesis"
    )


    resultado["recomendaciones"].append(
        "Confirmar normativa vigente aplicable"
    )


    return resultado



if __name__ == "__main__":

    print(
        revisar_informe(
            "Informe de prueba"
        )
    )
