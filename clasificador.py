def clasificar_respuestas(respuestas):
    # Ejemplo de cómo procesar las respuestas
    estilo_aprendizaje = "Visual" if respuestas.get("visual", False) else "No Visual"
    inteligencia = "Lógico-matemática" if respuestas.get("logico", False) else "Lingüística"
    personalidad = "Introvertido" if respuestas.get("introvertido", False) else "Extrovertido"

    return {
        "Estilo de Aprendizaje": estilo_aprendizaje,
        "Inteligencia Predominante": inteligencia,
        "Personalidad": personalidad,
    }
