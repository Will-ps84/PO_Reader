import re
from transformers import pipeline

model = pipeline("ner", model="models/ner_po", aggregation_strategy="simple")

po_re   = re.compile(r"^\d{8,12}$")
date_re = re.compile(r"\d{1,2}[/-]\d{1,2}[/-]\d{2,4}")

def extract(text: str) -> dict:
    ents = model(text)
    out = {"PO":[], "SKU":[], "QTY":[], "PRICE":[], "DATE":[], "INCOTERM":[]}
    for e in ents:
        label, word = e["entity_group"], e["word"].strip()
        if label=="PO" and po_re.match(word): out["PO"].append(word)
        elif label=="DATE" and date_re.match(word): out["DATE"].append(word)
        else: out[label].append(word)
    return {k: v[0] if v else None for k, v in out.items()}