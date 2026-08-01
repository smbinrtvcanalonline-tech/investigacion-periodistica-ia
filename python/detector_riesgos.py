# Detector de Riesgos Periodísticos IA
# Investigación Periodística IA

def detectar_riesgos(texto):

    alertas = []

    palabras_clave = [
        "irregularidad",
        "observación",
        "retraso",
        "sobrecosto",
        "incumplimiento"
    ]

    for palabra in palabras_clave:
        if palabra.lower() in texto.lower():
            alertas.append(
                f"Posible alerta encontrada: {palabra}"
            )

    resultado = {
        "cantidad_alertas": len(alertas),
        "alertas": alertas
    }

    return resultado


if __name__ == "__main__":

    documento = """
    Informe con observación por retraso
    y posible incumplimiento contractual.
    """

    informe = detectar_riesgos(documento)

    print(informe)
