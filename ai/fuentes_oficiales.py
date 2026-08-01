# ==================================================
# FUENTES OFICIALES PERÚ
# Investigación Periodística IA
# SMBINRTV
# ==================================================


FUENTES = {

    "presupuesto":
    "Ministerio de Economía y Finanzas - MEF",

    "contrataciones":
    "SEACE / OSCE",

    "control":
    "Contraloría General de la República",

    "normas":
    "Diario Oficial El Peruano",

    "justicia":
    "Poder Judicial y Ministerio Público",

    "transparencia":
    "Portal de Transparencia del Estado Peruano"

}



def obtener_fuentes():

    return FUENTES



def verificar_fuente(tipo):

    return FUENTES.get(
        tipo,
        "Fuente no registrada"
    )


if __name__ == "__main__":

    print(
        obtener_fuentes()
    )
