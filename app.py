import streamlit as st
from clasificador import clasificar_respuestas
from generador_pdf import generar_informe

# Función para inicializar el estado de las preguntas
def inicializar_estado():
    for categoria, lista_preguntas in preguntas.items():
        for i, pregunta in enumerate(lista_preguntas):
            clave = f"{categoria}_{i}"
            if clave not in st.session_state:
                st.session_state[clave] = "Sí"

# Preguntas del cuestionario
preguntas = {
    "Estilo de Aprendizaje": [
        "¿Te resulta más fácil aprender mediante gráficos o imágenes?",
        "¿Prefieres escuchar información en lugar de leerla?",
        "¿Te gusta aprender haciendo actividades prácticas?",
        "¿Recuerdas mejor lo que ves que lo que escuchas?",
        "¿Tiendes a mover tus manos o caminar mientras estudias?"
    ],
    "Inteligencias Múltiples": [
        "¿Disfrutas resolver problemas matemáticos o lógicos?",
        "¿Te gusta escribir, leer o contar historias?",
        "¿Te sientes conectado/a con la naturaleza o los animales?",
        "¿Tiendes a recordar canciones con facilidad?",
        "¿Prefieres trabajar en equipo y colaborar con otros?"
    ],
    "Personalidad": [
        "¿Prefieres trabajar solo/a en lugar de en equipo?",
        "¿Tiendes a tomar decisiones basadas en emociones más que en lógica?",
        "¿Te consideras una persona organizada y metódica?",
        "¿Tiendes a ser reservado/a sobre tus pensamientos o sentimientos?",
        "¿Sueles adaptarte fácilmente a cambios inesperados?"
    ],
}

# Configuración inicial de Streamlit
st.title("Agente Psicopedagógico")
st.write("Completa el siguiente cuestionario para determinar tu perfil psicopedagógico.")

# Inicializar el estado de las preguntas
inicializar_estado()

# Mostrar las preguntas y guardar respuestas
for categoria, lista_preguntas in preguntas.items():
    st.subheader(categoria)
    for i, pregunta in enumerate(lista_preguntas):
        clave = f"{categoria}_{i}"
        st.radio(
            pregunta,
            ["Sí", "No"],
            index=0 if st.session_state[clave] == "Sí" else 1,
            key=clave,  # Asocia directamente el valor al estado
        )

# Botón para procesar resultados
if st.button("Generar Informe"):
    respuestas = {clave: st.session_state[clave] for clave in st.session_state if clave.startswith("Estilo") or clave.startswith("Inteligencias") or clave.startswith("Personalidad")}
    perfil = clasificar_respuestas(respuestas)
    generar_informe(perfil)
    st.success("¡Informe generado con éxito!")
    st.download_button("Descargar Informe", data=open("informe.pdf", "rb"), file_name="Informe_Psicopedagógico.pdf")
