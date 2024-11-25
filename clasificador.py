def clasificar_respuestas(respuestas):
    # Inicializar contadores para cada categoría
    estilo_aprendizaje = {"Visual": 0, "Auditivo": 0, "Kinestésico": 0}
    inteligencias = {"Lógica": 0, "Lingüística": 0, "Naturalista": 0, "Musical": 0, "Interpersonal": 0}
    personalidad = {"Introvertido": 0, "Extrovertido": 0}

    # Clasificar respuestas
    for clave, respuesta in respuestas.items():
        if respuesta == "Sí":
            if "Estilo de Aprendizaje" in clave:
                if "0" in clave or "3" in clave:
                    estilo_aprendizaje["Visual"] += 1
                elif "1" in clave:
                    estilo_aprendizaje["Auditivo"] += 1
                elif "2" in clave or "4" in clave:
                    estilo_aprendizaje["Kinestésico"] += 1
            elif "Inteligencias Múltiples" in clave:
                if "0" in clave:
                    inteligencias["Lógica"] += 1
                elif "1" in clave:
                    inteligencias["Lingüística"] += 1
                elif "2" in clave:
                    inteligencias["Naturalista"] += 1
                elif "3" in clave:
                    inteligencias["Musical"] += 1
                elif "4" in clave:
                    inteligencias["Interpersonal"] += 1
            elif "Personalidad" in clave:
                if "0" in clave or "3" in clave:
                    personalidad["Introvertido"] += 1
                elif "1" in clave or "4" in clave:
                    personalidad["Extrovertido"] += 1

    # Determinar los resultados más altos
    estilo_aprendizaje_clasificado = max(estilo_aprendizaje, key=estilo_aprendizaje.get)
    inteligencia_clasificada = max(inteligencias, key=inteligencias.get)
    personalidad_clasificada = max(personalidad, key=personalidad.get)

    return {
        "Estilo de Aprendizaje": estilo_aprendizaje_clasificado,
        "Inteligencia Predominante": inteligencia_clasificada,
        "Personalidad": personalidad_clasificada,
    }
