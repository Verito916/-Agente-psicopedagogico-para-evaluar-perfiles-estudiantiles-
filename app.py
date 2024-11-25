import streamlit as st
from clasificador import clasificar_respuestas
from generador import generar_informe

# Título de la aplicación
st.title("Agente Psicopedagógico")

# Usar session_state para mantener las respuestas
if 'respuestas' not in st.session_state:
    st.session_state.respuestas = {}

# Función para almacenar respuestas en session_state
def guardar_respuesta(pregunta, respuesta):
    st.session_state.respuestas[pregunta] = respuesta

# Pregunta sobre el nivel de estudios
nivel_estudios = st.selectbox(
    "¿Cuál es tu nivel de estudios?", 
    ["Primaria", "Secundaria", "Pregrado", "Posgrado"],
    index=["Primaria", "Secundaria", "Pregrado", "Posgrado"].index(st.session_state.respuestas.get("nivel_estudios", "Primaria"))
)
guardar_respuesta("nivel_estudios", nivel_estudios)

# Pregunta sobre estilo de aprendizaje visual
visual = st.radio(
    "¿Prefieres aprender viendo imágenes o gráficos?", 
    ["Sí", "No"],
    index=0 if st.session_state.respuestas.get("estilo_aprendizaje_visual") == "Sí" else 1
)
guardar_respuesta("estilo_aprendizaje_visual", visual)

# Pregunta sobre estilo de aprendizaje auditivo
auditivo = st.radio(
    "¿Prefieres aprender escuchando información?", 
    ["Sí", "No"],
    index=0 if st.session_state.respuestas.get("estilo_aprendizaje_auditivo") == "Sí" else 1
)
guardar_respuesta("estilo_aprendizaje_auditivo", auditivo)

# Pregunta sobre estilo de aprendizaje kinestésico
kinestesico = st.radio(
    "¿Prefieres aprender mediante actividades físicas o prácticas?", 
    ["Sí", "No"],
    index=0 if st.session_state.respuestas.get("estilo_aprendizaje_kinestesico") == "Sí" else 1
)
guardar_respuesta("estilo_aprendizaje_kinestesico", kinestesico)

# Botón para clasificar el perfil
if st.button("Clasificar Perfil"):
    perfil = clasificar_respuestas(st.session_state.respuestas)
    st.write("Perfil clasificado:")
    st.json(perfil)
    
    # Generar informe PDF
    generar_informe(perfil)
