# ==================================================
# MODELO IA LOCAL
# Investigación Periodística IA
# SMBINRTV
# Conexión con Ollama
# ==================================================

import requests


def consultar_ia(prompt):

    url = "http://localhost:11434/api/generate"

    datos = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }

    try:

        respuesta = requests.post(
            url,
            json=datos
        )

        resultado = respuesta.json()

        return resultado.get(
            "response",
            "Sin respuesta del modelo"
        )


    except Exception as error:

        return (
            f"No se pudo conectar con IA local: {error}"
        )


if __name__ == "__main__":

    pregunta = """
    Analiza este documento como periodista
    de investigación peruano.
    """

    respuesta = consultar_ia(
        pregunta
    )

    print(respuesta)
