# ==================================================
# AGENTE DE INVESTIGACIÓN PERIODÍSTICA IA
# SMBINRTV
# ==================================================

from modelo_local import consultar_ia
from prompts_ia import obtener_prompt


def analizar_documento(texto):

    prompt_base = obtener_prompt()

    prompt_final = f"""
    {prompt_base}

    DOCUMENTO A ANALIZAR:

    {texto}

    Realiza un análisis profesional.
    """

    respuesta = consultar_ia(
        prompt_final
    )

    return respuesta



if __name__ == "__main__":

    documento = """
    Ejemplo de expediente público peruano
    para análisis periodístico.
    """

    resultado = analizar_documento(
        documento
    )

    print(resultado)
