from pathlib import Path
from src.data.pdf_to_text import pdf_to_text
from src.inference.post_process import extract

def predict_file(file_path: Path) -> dict:
    text = pdf_to_text(file_path)
    return extract(text)