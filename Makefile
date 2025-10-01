.PHONY: install run-api run-dash train docker-build docker-run

install:
	pip install -r requirements.txt

run-api:
	uvicorn src.api.main:app --reload --host 0.0.0.0 --port 8000

run-dash:
	streamlit run src/dashboard/app.py

train:
	python -m src.training.train_ner

docker-build:
	docker build -t po-reader .

docker-run:
	docker run -p 8000:8000 --env-file .env po-reader