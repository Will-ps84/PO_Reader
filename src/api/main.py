from fastapi import FastAPI, File, UploadFile
from src.inference.predictor import predict_file
import shutil, tempfile, pathlib

app = FastAPI(title="PO-Reader MVP")
@app.post("/predict")
def predict(file: UploadFile = File(...)):
    suf = pathlib.Path(file.filename).suffix
    with tempfile.NamedTemporaryFile(delete=False, suffix=suf) as tmp:
        shutil.copyfileobj(file.file, tmp)
        tmp_path = pathlib.Path(tmp.name)
    return predict_file(tmp_path)