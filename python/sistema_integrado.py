# ==================================================
# SISTEMA INTEGRADO DE INVESTIGACIÓN IA
# SMBINRTV - TÚ DECIDES
# ==================================================

from ai.agente_investigacion import analizar_documento
from ai.auditor_forense import auditar_informacion
from ai.informe_forense import crear_informe
from ai.evaluador_evidencia import evaluar_evidencia


def ejecutar_sistema(documento):

    resultado = {}

    resultado["evidencia"] = evaluar_evidencia(
        documento
    )


    resultado["analisis_ia"] = analizar_documento(
        documento
    )


    resultado["auditoria"] = auditar_informacion(
        documento
    )


    resultado["informe"] = crear_informe(
        resultado
    )


    return resultado



if __name__ == "__main__":

    documento = (
        "Expediente público de prueba"
    )

    informe = ejecutar_sistema(
        documento
    )

    print(informe)
