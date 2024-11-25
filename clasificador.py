def clasificar_respuestas(respuestas):
    # Lógica para clasificar el perfil del estudiante
    estilo_aprendizaje = "Visual" if respuestas["estilo_aprendizaje"]["visual"] else \
                         "Auditivo" if respuestas["estilo_aprendizaje"]["auditivo"] else "Kinestésico"

    inteligencia = "Lógico-matemática" if respuestas["estilo_aprendizaje"]["visual"] else \
                  "Lingüística" if respuestas["estilo_aprendizaje"]["auditivo"] else "Cinemática"

    personalidad = "Introvertido" if respuestas["estilo_aprendizaje"]["kinestesico"] else "Extrovertido"

    # Regresar el perfil clasificado
    perfil = {
        "Estilo de Aprendizaje": estilo_aprendizaje,
        "Inteligencia Predominante": inteligencia,
        "Personalidad": personalidad
    }

    return perfil
