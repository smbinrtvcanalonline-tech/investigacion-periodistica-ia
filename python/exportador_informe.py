# ==================================================
# EXPORTADOR DE INFORMES
# Investigación Periodística IA
# SMBINRTV
# ==================================================


def exportar_txt(informe, nombre):

    archivo = nombre + ".txt"

    with open(
        archivo,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(
            str(informe)
        )


    return archivo



def exportar_markdown(informe, nombre):

    archivo = nombre + ".md"

    contenido = f"""

# Informe de Investigación Periodística

{informe}

"""


    with open(
        archivo,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(
            contenido
        )


    return archivo



if __name__ == "__main__":

    ejemplo = {
        "titulo": "Investigación IA"
    }


    print(
        exportar_txt(
            ejemplo,
            "informe_prueba"
        )
    )
