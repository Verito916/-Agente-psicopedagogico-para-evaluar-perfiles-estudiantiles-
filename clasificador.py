def clasificar_respuestas(respuestas):
    estilo_aprendizaje = "Visual" if respuestas["estilo_aprendizaje"]["visual"] else \
                         "Auditivo" if respuestas["estilo_aprendizaje"]["auditivo"] else "Kinestésico"

    inteligencia = max(respuestas["inteligencias"], key=lambda x: respuestas["inteligencias"][x])

    personalidad = "Introvertido" if respuestas["personalidad"]["introversion"] else "Extrovertido"

    iq_score = sum(respuestas["iq"]) * 50  # Valor estimado por pregunta correcta

    return {
        "estilo_aprendizaje": estilo_aprendizaje,
        "inteligencia": inteligencia,
        "personalidad": personalidad,
        "iq_score": iq_score
    }
