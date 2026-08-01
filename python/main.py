# ==================================================
# MOTOR PRINCIPAL
# Investigación Periodística IA
# SMBINRTV - TÚ DECIDES
# ==================================================

from sistema_integrado import ejecutar_sistema
from exportador_informe import exportar_markdown


def iniciar_investigacion():

    documento = input(
        "Ingrese documento o información a analizar: "
    )


    resultado = ejecutar_sistema(
        documento
    )


    archivo = exportar_markdown(
        resultado,
        "informe_investigacion"
    )


    print("\nInvestigación completada")
    print(
        "Informe generado:",
        archivo
    )



if __name__ == "__main__":

    iniciar_investigacion()
