# Generador de Noticia Periodística IA
# Investigación Periodística IA
# SMBINRTV

def generar_noticia(datos):

    noticia = {
        "titulo": "",
        "bajada": "",
        "desarrollo": "",
        "hallazgos": []
    }

    noticia["titulo"] = (
        "Análisis periodístico generado por IA"
    )

    noticia["bajada"] = (
        "Documento analizado bajo criterios "
        "periodísticos, económicos y legales."
    )

    noticia["desarrollo"] = datos

    noticia["hallazgos"].append(
        "Revisar documentación oficial antes de publicar"
    )

    return noticia


if __name__ == "__main__":

    resultado = generar_noticia(
        "Ejemplo de investigación"
    )

    print(resultado)
