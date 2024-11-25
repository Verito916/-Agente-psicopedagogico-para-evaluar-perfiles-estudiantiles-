import streamlit as st
from clasificador import clasificar_respuestas
from generador import generar_informe

# Título de la aplicación
st.title("Agente Psicopedagógico")

# Formulario para que el usuario ingrese sus respuestas
nivel_estudios = st.selectbox("¿Cuál es tu nivel de estudios?", ["Primaria", "Secundaria", "Bachillerato", "Universidad"])
visual = st.radio("¿Prefieres aprender viendo imágenes o gráficos?", ["Sí", "No"]) == "Sí"
auditivo = st.radio("¿Prefieres aprender escuchando información?", ["Sí", "No"]) == "Sí"
kinestesico = st.radio("¿Prefieres aprender mediante actividades físicas o prácticas?", ["Sí", "No"]) == "Sí"

# Almacenar las respuestas en session_state para no perderlas al recargar la página
if 'respuestas' not in st.session_state:
    st.session_state.respuestas = {}

st.session_state.respuestas["nivel_estudios"] = nivel_estudios
st.session_state.respuestas["estilo_aprendizaje"] = {"visual": visual, "auditivo": auditivo, "kinestesico": kinestesico}

# Mostrar las preguntas
st.write("Nivel de estudios:", st.session_state.respuestas["nivel_estudios"])
st.write("Estilo de aprendizaje:", st.session_state.respuestas["estilo_aprendizaje"])

# Botón para clasificar el perfil
if st.button("Clasificar Perfil"):
    perfil = clasificar_respuestas(st.session_state.respuestas)
    st.write("Perfil clasificado:", perfil)

    # Generar el informe
    if st.button("Generar Informe"):
        informe = generar_informe(st.session_state.respuestas)
        st.write(informe)
