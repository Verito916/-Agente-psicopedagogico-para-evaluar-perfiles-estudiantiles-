from clasificador import clasificar_respuestas

# Supongamos que "respuestas" se llena mediante el cuestionario
respuestas = {
    "visual": st.radio("¿Prefieres aprender viendo imágenes o gráficos?", ["Sí", "No"]) == "Sí",
    "logico": st.radio("¿Te gusta resolver problemas matemáticos?", ["Sí", "No"]) == "Sí",
    "introvertido": st.radio("¿Prefieres trabajar solo?", ["Sí", "No"]) == "Sí",
}

# Clasificar respuestas
perfil = clasificar_respuestas(respuestas)
st.write("Perfil clasificado:", perfil)
