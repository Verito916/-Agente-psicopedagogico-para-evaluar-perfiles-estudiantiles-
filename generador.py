from fpdf import FPDF

def generar_informe(nombre, carrera, nivel, resultados):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Informe Psicopedagógico", ln=True, align="C")
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Estudiante: {nombre}", ln=True)
    pdf.cell(200, 10, txt=f"Carrera: {carrera}", ln=True)
    pdf.cell(200, 10, txt=f"Nivel: {nivel}", ln=True)
    pdf.ln(10)
    pdf.cell(200, 10, txt="Resultados:", ln=True)
    pdf.cell(200, 10, txt=f"Estilo de Aprendizaje: {resultados['estilo_aprendizaje']}", ln=True)
    pdf.cell(200, 10, txt=f"Inteligencia Predominante: {resultados['inteligencia']}", ln=True)
    pdf.cell(200, 10, txt=f"Personalidad: {resultados['personalidad']}", ln=True)
    pdf.cell(200, 10, txt=f"Estimación de IQ: {resultados['iq_score']}", ln=True)
    pdf.output("informe_estudiante.pdf")
