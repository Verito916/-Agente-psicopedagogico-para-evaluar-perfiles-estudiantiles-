import streamlit as st
from clasificador import clasificar_respuestas  # Asegúrate de que este import esté correcto

# Crear el cuestionario
respuestas = {
    "visual": st.radio("¿Prefieres aprender viendo imágenes o gráficos?", ["Sí", "No"]) == "Sí",
    "logico": st.radio("¿Te gusta resolver problemas matemáticos?", ["Sí", "No"]) == "Sí",
    "introvertido": st.radio("¿Prefieres trabajar solo?", ["Sí", "No"]) == "Sí",
}

# Clasificar respuestas
perfil = clasificar_respuestas(respuestas)

# Mostrar el perfil
st.write("Perfil clasificado:", perfil)
