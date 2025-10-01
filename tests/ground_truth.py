import pandas as pd
import pathlib
import random
import datetime

# Usa ruta absoluta para evitar confusiones
DATA_DIR = pathlib.Path(r"C:\Dev\PO_reader\data\raw")
TEST_PDFS = list(DATA_DIR.glob("po_*.pdf"))[:20]   # 20 primeros

GROUND = []
for pdf in TEST_PDFS:
    # >>>>>>>>>>  AJUSTA AQUÍ CON VALORES REALES  <<<<<<<<<<
    # Abre el PDF y copia los valores reales; aquí uso dummy para que corra
    GROUND.append({
        "archivo": pdf.name,
        "PO":      pdf.stem.replace("po_", "") + "-2025",
        "SKU":     "Producto-" + pdf.stem[-2:],
        "QTY":     str(random.randint(10, 500)),
        "PRICE":   f"{random.randint(1, 100)}.{random.randint(0, 99):02d}",
        "DATE":    (datetime.date.today() + datetime.timedelta(days=random.randint(1, 60))).strftime("%d/%m/%Y"),
        "INCOTERM": random.choice(["FOB", "CIF", "EXW"]),
    })

df = pd.DataFrame(GROUND)
df.to_excel("tests/ground_truth.xlsx", index=False)
print("✅ tests/ground_truth.xlsx creado con 20 filas.")