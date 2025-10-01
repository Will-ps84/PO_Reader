import os, json, numpy as np
from datasets import load_dataset, DatasetDict
from transformers import (AutoTokenizer, AutoModelForTokenClassification,
                          DataCollatorForTokenClassification, TrainingArguments, Trainer)
from src.training.utils import load_doccano

model_name = os.getenv("MODEL_NAME", "xlm-roberta-base")
tokenizer = AutoTokenizer.from_pretrained(model_name, add_prefix_space=True)
raw_ds = load_doccano("data/processed/train.jsonl")
label_list = sorted({tag for ex in raw_ds for tag in ex["ner_tags"]})
label2id = {l: i for i, l in enumerate(label_list)}

def tokenize_and_align(ex):
    tokenized = tokenizer(ex["tokens"], truncation=True, is_split_into_words=True)
    labels = []
    for i, label in enumerate(ex["ner_tags"]):
        word_ids = tokenized.word_ids(batch_index=i)
        previous_word_idx = None
        label_ids = []
        for word_idx in word_ids:
            if word_idx is None: label_ids.append(-100)
            elif word_idx != previous_word_idx: label_ids.append(label2id[label[word_idx]])
            else: label_ids.append(-100)
            previous_word_idx = word_idx
        labels.append(label_ids)
    tokenized["labels"] = labels
    return tokenized

tokenized_ds = raw_ds.map(tokenize_and_align, batched=True)
model = AutoModelForTokenClassification.from_pretrained(
            model_name, num_labels=len(label_list), id2label={i: l for l, i in label2id.items()})
args = TrainingArguments(
        output_dir="models/ner_po",
        evaluation_strategy="epoch",
        learning_rate=2e-5,
        per_device_train_batch_size=16,
        num_train_epochs=5,
        weight_decay=0.01,
        seed=int(os.getenv("SEED", 42)),
)
trainer = Trainer(model, args, train_dataset=tokenized_ds,
                  data_collator=DataCollatorForTokenClassification(tokenizer),
                  tokenizer=tokenizer)
trainer.train()
trainer.save_model("models/ner_po")
tokenizer.save_pretrained("models/ner_po")