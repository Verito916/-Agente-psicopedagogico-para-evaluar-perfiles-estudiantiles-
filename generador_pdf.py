from fpdf import FPDF

def generar_informe(perfil):
    # Crear el documento PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Informe Psicopedagógico", ln=True, align='C')

    # Validar y agregar los datos del perfil
    if "Estilo de Aprendizaje" in perfil:
        pdf.cell(200, 10, txt=f"Estilo de Aprendizaje: {perfil['Estilo de Aprendizaje']}", ln=True)
    else:
        pdf.cell(200, 10, txt="Estilo de Aprendizaje: No disponible", ln=True)

    if "Inteligencia Predominante" in perfil:
        pdf.cell(200, 10, txt=f"Inteligencia Predominante: {perfil['Inteligencia Predominante']}", ln=True)
    else:
        pdf.cell(200, 10, txt="Inteligencia Predominante: No disponible", ln=True)

    if "Personalidad" in perfil:
        pdf.cell(200, 10, txt=f"Personalidad: {perfil['Personalidad']}", ln=True)
    else:
        pdf.cell(200, 10, txt="Personalidad: No disponible", ln=True)

    # Guardar el archivo PDF
    pdf.output("informe_psicopedagogico.pdf")
