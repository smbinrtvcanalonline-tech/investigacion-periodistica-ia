# Interfaz Web
# Investigación Periodística IA
# SMBINRTV

import streamlit as st


st.title("Investigación Periodística IA")

st.subheader(
    "Sistema de análisis forense para periodismo de investigación"
)


archivo = st.file_uploader(
    "Suba un documento PDF",
    type=["pdf"]
)


if archivo:

    st.success(
        "Documento recibido correctamente"
    )

    st.write(
        "El sistema analizará el documento y generará:"
    )

    st.write(
        "- Resumen ejecutivo"
    )

    st.write(
        "- Posibles riesgos"
    )

    st.write(
        "- Análisis periodístico"
    )
