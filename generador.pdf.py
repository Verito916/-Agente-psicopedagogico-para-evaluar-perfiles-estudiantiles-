from fpdf import FPDF

def generar_informe(perfil):
    # Crear objeto PDF
    pdf = FPDF()
    pdf.add_page()
    
    # Título
    pdf.set_font("Arial", size=16)
    pdf.cell(200, 10, txt="Informe Psicopedagógico", ln=True, align='C')

    # Contenido del informe
    pdf.set_font("Arial", size=12)
    for clave, valor in perfil.items():
        pdf.ln(10)
        pdf.cell(200, 10, txt=f"{clave}: {valor}", ln=True)

    # Guardar el archivo
    pdf.output("informe_psicopedagogico.pdf")
    print("Informe PDF generado correctamente.")
