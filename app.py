import streamlit as st
from clasificador import clasificar_respuestas
from generador_pdf import generar_informe

# Función para mantener las respuestas en el estado
def guardar_respuesta(clave, valor):
    if clave not in st.session_state:
        st.session_state[clave] = valor
    else:
        st.session_state[clave] = valor

# Configuración inicial
st.title("Agente Psicopedagógico")
st.write("Completa el siguiente cuestionario para determinar tu perfil psicopedagógico.")

# Preguntas del cuestionario
preguntas = {
    "Estilo de Aprendizaje": [
        "¿Te resulta más fácil aprender mediante gráficos o imágenes?",
        "¿Prefieres escuchar información en lugar de leerla?",
        "¿Te gusta aprender haciendo actividades prácticas?"
    ],
    "Inteligencias Múltiples": [
        "¿Disfrutas resolver problemas matemáticos o lógicos?",
        "¿Te gusta escribir, leer o contar historias?",
        "¿Te sientes conectado/a con la naturaleza o los animales?"
    ],
    "Personalidad": [
        "¿Prefieres trabajar solo/a en lugar de en equipo?",
        "¿Tiendes a tomar decisiones basadas en emociones más que en lógica?",
        "¿Te consideras una persona organizada y metódica?"
    ],
}

# Mostrar preguntas y guardar respuestas
for categoria, lista_preguntas in preguntas.items():
    st.subheader(categoria)
    for i, pregunta in enumerate(lista_preguntas):
        clave = f"{categoria}_{i}"
        respuesta = st.radio(
            pregunta,
            ["Sí", "No"],
            key=clave,
            index=0 if clave not in st.session_state else ["Sí", "No"].index(st.session_state[clave]),
            on_change=guardar_respuesta,
            args=(clave, st.session_state.get(clave, "Sí")),
        )

# Botón para procesar resultados
if st.button("Generar Informe"):
    respuestas = {clave: st.session_state[clave] for clave in st.session_state}
    perfil = clasificar_respuestas(respuestas)
    generar_informe(perfil)
    st.success("¡Informe generado con éxito!")
    st.download_button("Descargar Informe", data=open("informe.pdf", "rb"), file_name="Informe_Psicopedagógico.pdf")
