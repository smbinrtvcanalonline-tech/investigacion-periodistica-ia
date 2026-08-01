# Analizador Económico Presupuestal
# Investigación Periodística IA
# Perú

def analizar_presupuesto(datos):

    resultado = {
        "analisis": [],
        "alertas": []
    }

    if datos.get("pim"):

        resultado["analisis"].append(
            f"PIM registrado: {datos['pim']}"
        )

    if datos.get("devengado"):

        porcentaje = (
            datos["devengado"] /
            datos["pim"]
        ) * 100

        resultado["analisis"].append(
            f"Ejecución financiera aproximada: {porcentaje:.2f}%"
        )

        if porcentaje < 50:

            resultado["alertas"].append(
                "Baja ejecución presupuestal requiere revisión"
            )

    return resultado


if __name__ == "__main__":

    ejemplo = {
        "pim": 1000000,
        "devengado": 300000
    }

    print(
        analizar_presupuesto(ejemplo)
    )
