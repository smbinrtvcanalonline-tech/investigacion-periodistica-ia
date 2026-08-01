# ==================================================
# BASE LEGAL PERUANA
# Investigación Periodística IA
# SMBINRTV
# ==================================================

import json


def cargar_normativa():

    try:

        with open(
            "legal/normativa_peru.json",
            "r",
            encoding="utf-8"
        ) as archivo:

            datos = json.load(
                archivo
            )

        return datos


    except Exception as error:

        return {
            "error": str(error)
        }



def validar_referencia_legal():

    normativa = cargar_normativa()

    reglas = normativa.get(
        "reglas",
        {}
    )

    return reglas



if __name__ == "__main__":

    print(
        validar_referencia_legal()
    )
