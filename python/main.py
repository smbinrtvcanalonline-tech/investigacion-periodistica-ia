# Sistema Principal
# Investigación Periodística IA
# SMBINRTV

from analizador_pdf import analizar_pdf
from resumen_ia import generar_resumen
from detector_riesgos import detectar_riesgos


def ejecutar_investigacion(documento):

    print("=== INVESTIGACIÓN PERIODÍSTICA IA ===")

    print("\n1. Analizando documento...")
    analisis = analizar_pdf(documento)

    print(analisis)

    print("\n2. Generando resumen...")
    resumen = generar_resumen(documento)

    print(resumen)

    print("\n3. Detectando riesgos...")
    riesgos = detectar_riesgos(documento)

    print(riesgos)

    return {
        "analisis": analisis,
        "resumen": resumen,
        "riesgos": riesgos
    }


if __name__ == "__main__":

    archivo = "documento_prueba.pdf"

    resultado = ejecutar_investigacion(archivo)

    print("\nProceso terminado.")
