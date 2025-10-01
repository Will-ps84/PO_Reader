import pandas as pd
import requests
import pathlib as Path
import datetime

URL = "http://localhost:8000/predict"
GROUND = pd.read_excel("tests/ground_truth.xlsx")
RESULTS = []

for _, row in GROUND.iterrows():
    file = Path.Path(r"C:\Dev\PO_reader\data\raw") / row["archivo"]
    r = requests.post(URL, files={"file": open(file, "rb")})
    pred = r.json()
    RESULTS.append({
        "archivo": row["archivo"],
        "PO_pred": pred.get("PO"),
        "PO_true": row["PO"],
        "SKU_pred": pred.get("SKU"),
        "SKU_true": row["SKU"],
        "QTY_pred": pred.get("QTY"),
        "QTY_true": row["QTY"],
        "PRICE_pred": pred.get("PRICE"),
        "PRICE_true": row["PRICE"],
        "DATE_pred": pred.get("DATE"),
        "DATE_true": row["DATE"],
        "INCOTERM_pred": pred.get("INCOTERM"),
        "INCOTERM_true": row["INCOTERM"],
    })

df = pd.DataFrame(RESULTS)
for col in ["PO", "SKU", "QTY", "PRICE", "DATE", "INCOTERM"]:
    df[f"{col}_ok"] = df[f"{col}_pred"] == df[f"{col}_true"]

accuracy = df[[c for c in df.columns if c.endswith("_ok")]].mean()
print("Accuracy por campo:\n", accuracy)
print(f"Global: {accuracy.mean():.1%}")
df.to_excel("tests/resultados.xlsx", index=False)
print("✅ Resultados guardados en tests/resultados.xlsx")