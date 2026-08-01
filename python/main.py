# ==================================================
# SISTEMA DE INVESTIGACIÓN PERIODÍSTICA IA
# SMBINRTV
# Orquestador principal
# ==================================================

from analizador_pdf import analizar_pdf
from resumen_ia import generar_resumen
from detector_riesgos import detectar_riesgos
from verificador_normativo import verificar_norma
from analizador_economico import analizar_presupuesto
from generador_noticia import generar_noticia


def ejecutar_investigacion(documento, datos_presupuesto):

    print("=" * 50)
    print("INVESTIGACIÓN PERIODÍSTICA IA")
    print("=" * 50)


    print("\n[1] Analizando documento PDF...")
    analisis_pdf = analizar_pdf(documento)


    print("\n[2] Generando resumen...")
    resumen = generar_resumen(documento)


    print("\n[3] Detectando posibles riesgos...")
    riesgos = detectar_riesgos(documento)


    print("\n[4] Verificando marco legal...")
    marco_legal = verificar_norma(
        "Normativa peruana vigente"
    )


    print("\n[5] Analizando presupuesto...")
    analisis_economico = analizar_presupuesto(
        datos_presupuesto
    )


    print("\n[6] Generando noticia...")
    
    informe = {
        "documento": analisis_pdf,
        "resumen": resumen,
        "riesgos": riesgos,
        "legal": marco_legal,
        "economico": analisis_economico
    }


    noticia = generar_noticia(
        informe
    )


    return noticia



if __name__ == "__main__":


    documento_prueba = "expediente.pdf"


    presupuesto = {
        "pim": 1000000,
        "devengado": 300000
    }


    resultado = ejecutar_investigacion(
        documento_prueba,
        presupuesto
    )


    print("\nRESULTADO FINAL")
    print(resultado)
