# ==================================================
# CONTROLADOR DEL SISTEMA
# Investigación Periodística IA
# SMBINRTV
# ==================================================

from sistema_integrado import ejecutar_sistema
from exportador_informe import exportar_markdown



def procesar_investigacion(documento):

    resultado = ejecutar_sistema(
        documento
    )


    archivo = exportar_markdown(
        resultado,
        "informe_generado"
    )


    return {

        "resultado": resultado,

        "archivo": archivo

    }



if __name__ == "__main__":

    prueba = procesar_investigacion(
        "Documento de prueba"
    )

    print(prueba)
