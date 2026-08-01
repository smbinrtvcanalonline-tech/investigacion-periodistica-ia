# Pruebas del Sistema
# Investigación Periodística IA
# SMBINRTV


from python.detector_riesgos import detectar_riesgos
from python.verificador_normativo import verificar_norma
from python.analizador_economico import analizar_presupuesto


def test_detector_riesgos():

    resultado = detectar_riesgos(
        "Existe retraso e incumplimiento"
    )

    assert resultado["cantidad_alertas"] > 0



def test_verificador_normativo():

    resultado = verificar_norma(
        "Norma peruana",
        True
    )

    assert resultado["estado"] != ""



def test_analisis_economico():

    datos = {
        "pim": 1000000,
        "devengado": 500000
    }

    resultado = analizar_presupuesto(datos)

    assert len(resultado["analisis"]) > 0
