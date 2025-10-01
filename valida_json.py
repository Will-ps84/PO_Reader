import json

def validate_jsonl(file_path):
    with open(file_path, "r", encoding="utf-8-sig") as f:  # 👈 utf-8-sig
        for i, line in enumerate(f, start=1):
            try:
                obj = json.loads(line)
                # Verificar que "label" siempre sea lista
                if not isinstance(obj.get("label", []), list):
                    print(f"⚠️ Línea {i}: 'label' no es lista -> {obj}")
            except json.JSONDecodeError as e:
                print(f"❌ JSON inválido en línea {i}: {e}")
                return False
    print("✅ El archivo JSONL es válido y está limpio.")
    return True

# Usa la función
validate_jsonl("C:/Dev/PO_reader/data/processed/train.jsonl")

