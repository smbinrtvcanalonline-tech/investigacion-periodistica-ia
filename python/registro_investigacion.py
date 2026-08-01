# ==================================================
# REGISTRO DE INVESTIGACIONES
# SMBINRTV - TÚ DECIDES
# ==================================================

import json
import datetime


ARCHIVO = "investigaciones.json"



def guardar_investigacion(datos):

    registro = {

        "fecha":
        str(datetime.datetime.now()),

        "datos":
        datos

    }


    try:

        with open(
            ARCHIVO,
            "r",
            encoding="utf-8"
        ) as archivo:

            historial = json.load(
                archivo
            )


    except:

        historial = []


    historial.append(
        registro
    )


    with open(
        ARCHIVO,
        "w",
        encoding="utf-8"
    ) as archivo:

        json.dump(
            historial,
            archivo,
            indent=4,
            ensure_ascii=False
        )


    return True



def obtener_historial():

    try:

        with open(
            ARCHIVO,
            "r",
            encoding="utf-8"
        ) as archivo:

            return json.load(
                archivo
            )

    except:

        return []



if __name__ == "__main__":

    guardar_investigacion(
        "Prueba del sistema"
    )

    print(
        obtener_historial()
    )
