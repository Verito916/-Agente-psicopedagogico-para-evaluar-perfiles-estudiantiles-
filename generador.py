# generador.py

def generar_informe(perfil):
    # Lógica para generar el informe PDF o el documento que necesites
    # Este es solo un ejemplo básico de cómo podrías generar un informe:
    with open("informe.txt", "w") as f:
        f.write(str(perfil))  # Escribe el perfil como texto en un archivo
