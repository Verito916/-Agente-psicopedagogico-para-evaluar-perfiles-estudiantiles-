from clasificador import clasificar_respuestas

# Clasificación
perfil = clasificar_respuestas(respuestas)

# Verificar el contenido de perfil antes de generar el informe
st.write("Perfil clasificado:", perfil)

# Generar informe en PDF
generar_informe(perfil)
