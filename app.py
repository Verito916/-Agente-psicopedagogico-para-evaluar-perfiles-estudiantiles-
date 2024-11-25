import streamlit as st
from clasificador import clasificar_respuestas
from generador_pdf import generar_informe

# Usar session_state para mantener el estado de las respuestas
if 'respuestas' not in st.session_state:
    st.session_state.respuestas = {}

# Preguntar por los datos iniciales (nivel de estudios, nombre, edad, semestre, carrera, etc.)
st.title("Agente Psicopedagógico")

# Nivel de estudios
if 'nivel_estudios' not in st.session_state.respuestas:
    st.session_state.respuestas['nivel_estudios'] = st.selectbox(
        "¿Cuál es tu nivel de estudios?",
        ["Primaria", "Secundaria", "Universidad", "Posgrado"]
    )

# Pregunta sobre el estilo de aprendizaje
if 'estilo_aprendizaje' not in st.session_state.respuestas:
    st.session_state.respuestas['estilo_aprendizaje'] = {}
    st.session_state.respuestas['estilo_aprendizaje']['visual'] = st.radio(
        "¿Prefieres aprender viendo imágenes o gráficos?", ["Sí", "No"]
    ) == "Sí"
    st.session_state.respuestas['estilo_aprendizaje']['auditivo'] = st.radio(
        "¿Prefieres aprender escuchando información?", ["Sí", "No"]
    ) == "Sí"
    st.session_state.respuestas['estilo_aprendizaje']['kinestesico'] = st.radio(
        "¿Prefieres aprender mediante actividades físicas o prácticas?", ["Sí", "No"]
    ) == "Sí"

# Guardar las respuestas al clasificador
if st.button("Clasificar Perfil"):
    perfil = clasificar_respuestas(st.session_state.respuestas)
    st.write("Perfil clasificado:", perfil)

    # Generar el informe en PDF
    generar_informe(perfil)
