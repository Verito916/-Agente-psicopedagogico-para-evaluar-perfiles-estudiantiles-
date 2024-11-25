import streamlit as st
from clasificador import clasificar_respuestas
from generador_pdf import generar_informe

# Configuración inicial
st.set_page_config(page_title="Agente Psicopedagógico", layout="centered")

# Título de la aplicación
st.title("Agente Psicopedagógico")
st.write("Responde el cuestionario para obtener tu perfil psicopedagógico.")

# Formulario de identificación
with st.form(key="identificacion"):
    nombre = st.text_input("Nombre:")
    carrera = st.text_input("Carrera:")
    nivel = st.selectbox("Nivel Académico:", ["1er semestre", "2do semestre", "3er semestre", "Otro"])
    submit_id = st.form_submit_button("Siguiente")

# Si el usuario ha llenado sus datos, avanza al cuestionario
if submit_id:
    st.write(f"¡Hola, {nombre}! Completemos el cuestionario.")

    # Sección de preguntas
    respuestas = {}
    respuestas["estilo_aprendizaje"] = {
        "visual": st.radio("¿Prefieres aprender viendo gráficos o imágenes?", ["Sí", "No"]) == "Sí",
        "auditivo": st.radio("¿Prefieres escuchar explicaciones o discusiones?", ["Sí", "No"]) == "Sí",
        "kinestesico": st.radio("¿Prefieres actividades prácticas?", ["Sí", "No"]) == "Sí"
    }

    respuestas["inteligencias"] = {
        "lingüística": st.radio("¿Disfrutas escribir o leer?", ["Sí", "No"]) == "Sí",
        "matemática": st.radio("¿Te gustan los acertijos matemáticos?", ["Sí", "No"]) == "Sí",
        "espacial": st.radio("¿Disfrutas dibujar o visualizar ideas?", ["Sí", "No"]) == "Sí",
        "musical": st.radio("¿Te interesa tocar instrumentos?", ["Sí", "No"]) == "Sí"
    }

    respuestas["personalidad"] = {
        "introversion": st.radio("¿Prefieres espacios tranquilos?", ["Sí", "No"]) == "Sí",
        "extroversion": st.radio("¿Disfrutas actividades sociales?", ["Sí", "No"]) == "Sí"
    }

    respuestas["iq"] = [
        st.radio("Si 2+2=4, ¿cuánto es 5x2?", ["10", "12", "15"]) == "10",
        st.radio("Completa la secuencia: 2, 4, 8, ...", ["16", "32", "64"]) == "32"
    ]

    # Botón para generar informe
    if st.button("Generar Informe"):
        resultados = clasificar_respuestas(respuestas)
        generar_informe(nombre, carrera, nivel, resultados)
        st.success("Informe generado. Descárgalo abajo.")
        with open("informe_estudiante.pdf", "rb") as pdf:
            st.download_button("Descargar Informe", pdf, "informe_estudiante.pdf")
