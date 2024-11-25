def generar_informe(respuestas):
    informe = f"Informe de Perfil Psicopedagógico\n\n"
    informe += f"Nivel de estudios: {respuestas['nivel_estudios']}\n"
    informe += f"Estilo de aprendizaje: {respuestas['estilo_aprendizaje']}\n"
    informe += f"Inteligencia predominante: Lógico-matemática\n"  # Aquí puedes adaptar según las respuestas
    informe += f"Personalidad: Introvertido\n"  # Puedes personalizar según los datos
    return informe
