# ==================================================
# INTERFAZ PERIODÍSTICA IA
# SMBINRTV - TÚ DECIDES
# ==================================================

import tkinter as tk
from tkinter import filedialog, messagebox


class AplicacionInvestigacion:


    def __init__(self, ventana):

        self.ventana = ventana

        self.ventana.title(
            "Auditor Forense Periodístico IA - SMBINRTV"
        )

        self.ventana.geometry(
            "700x400"
        )


        self.documento = ""


        boton_cargar = tk.Button(
            ventana,
            text="Cargar Documento",
            command=self.cargar_documento
        )

        boton_cargar.pack(
            pady=20
        )


        boton_iniciar = tk.Button(
            ventana,
            text="Iniciar Investigación IA",
            command=self.iniciar
        )

        boton_iniciar.pack(
            pady=20
        )


        self.resultado = tk.Label(
            ventana,
            text="Esperando documento..."
        )

        self.resultado.pack(
            pady=20
        )



    def cargar_documento(self):

        archivo = filedialog.askopenfilename()

        self.documento = archivo

        self.resultado.config(
            text="Documento cargado"
        )



    def iniciar(self):

        if self.documento:

            self.resultado.config(
                text="Análisis iniciado..."
            )

        else:

            messagebox.showwarning(
                "Aviso",
                "Debe cargar un documento"
            )



if __name__ == "__main__":

    ventana = tk.Tk()

    app = AplicacionInvestigacion(
        ventana
    )

    ventana.mainloop()
