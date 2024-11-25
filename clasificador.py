def clasificar_respuestas(respuestas):
    estilo_aprendizaje = "Visual" if respuestas["estilo_aprendizaje"]["visual"] else \
                         "Auditivo" if respuestas["estilo_aprendizaje"]["auditivo"] else \
                         "Kinestésico" if respuestas["estilo_aprendizaje"]["kinestesico"] else "Desconocido"
    
    # Aquí puedes agregar más lógica según sea necesario
    return {
        "Estilo de Aprendizaje": estilo_aprendizaje,
        "Inteligencia Predominante": "Lógico-matemática",  # Aquí podrías agregar lógica para detectar la inteligencia
        "Personalidad": "Introvertido"  # Lo mismo para la personalidad
    }
