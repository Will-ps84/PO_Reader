from pathlib import Path
from fpdf import FPDF
from fpdf.enums import XPos, YPos

TXT_DIR = Path(r'C:\Users\WILI\OneDrive\Escritorio\Ciencia de Datos, AI, Machine Learning\Visual Code\Introducción Machine Learning\PO_reader\data\raw')
PDF_DIR = TXT_DIR

class PO_PDF(FPDF):
    def header(self):
        self.set_font('Helvetica', 'B', 10)  # Helvetica disponible siempre
        self.cell(0, 6, 'PURCHASE ORDER', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
        self.ln(1)

def txt_to_pdf(txt_file: Path):
    pdf = PO_PDF()
    pdf.set_left_margin(2)   # 2 mm ¡muy estrecho!
    pdf.set_right_margin(2)
    pdf.set_auto_page_break(auto=True, margin=5)
    pdf.add_page()

    lines = txt_file.read_text(encoding="utf-8").splitlines()
    pdf.set_font('Helvetica', size=7)        # fuente pequeña
    for line in lines:
        # Ancho fijo 200 mm (casi página completa), salto automático
        pdf.multi_cell(200, 3, line.strip(), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(1)

    pdf.set_font('Helvetica', 'I', size=6)
    pdf.cell(200, 4, "Incoterm: FOB", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(200, 4, "Date: 15-08-2025", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    out_file = txt_file.with_suffix(".pdf")
    pdf.output(out_file)
    print(f"✅ {out_file.name} creado")

def batch_convert():
    for txt in TXT_DIR.glob("*.txt"):
        txt_to_pdf(txt)

if __name__ == "__main__":
    batch_convert()