from datasets import load_dataset
def load_doccano(path):
    return load_dataset("json", data_files=path, split="train")