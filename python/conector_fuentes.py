# ==================================================
# CONECTOR DE FUENTES PÚBLICAS
# Investigación Periodística IA
# SMBINRTV
# ==================================================


FUENTES_PUBLICAS = {

    "MEF":
    "Presupuesto y ejecución pública",

    "SEACE":
    "Contrataciones del Estado",

    "CONTRALORIA":
    "Informes de control",

    "TRANSPARENCIA":
    "Información pública estatal",

    "EL_PERUANO":
    "Normativa oficial"

}



def listar_fuentes():

    return FUENTES_PUBLICAS



def consultar_fuente(nombre):

    return FUENTES_PUBLICAS.get(
        nombre,
        "Fuente no registrada"
    )



if __name__ == "__main__":

    print(
        listar_fuentes()
    )
