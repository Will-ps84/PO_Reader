import tempfile
from pathlib import Path
from PO_reader.txt2pdf import txt_to_pdf

def test_txt_to_pdf_creates_pdf():
    # Crear un archivo .txt temporal con contenido de prueba
    with tempfile.TemporaryDirectory() as tmpdir:
        txt_path = Path(tmpdir) / "prueba.txt"
        txt_path.write_text("Línea 1\nLínea 2\nLínea 3", encoding="utf-8")
        
        # Ejecutar la función para convertir a PDF
        txt_to_pdf(txt_path)
        
        # Verificar que el PDF se creó
        pdf_path = txt_path.with_suffix(".pdf")
        assert pdf_path.exists(), "El archivo PDF no se creó"
        assert pdf_path.stat().st_size > 0, "El archivo PDF está vacío"