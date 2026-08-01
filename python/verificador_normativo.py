# Verificador Normativo Peruano
# Investigacion Periodistica IA

def verificar_norma(nombre_norma, vigente=True):

    resultado = {
        "norma": nombre_norma,
        "estado": "",
        "observacion": ""
    }

    if vigente:

        resultado["estado"] = "Norma registrada como vigente"
        resultado["observacion"] = (
            "Debe confirmarse en fuentes oficiales antes de citarla"
        )

    else:

        resultado["estado"] = "No utilizar"
        resultado["observacion"] = (
            "La norma no debe citarse sin verificar su vigencia"
        )

    return resultado


if __name__ == "__main__":

    prueba = verificar_norma(
        "Normativa peruana"
    )

    print(prueba)
