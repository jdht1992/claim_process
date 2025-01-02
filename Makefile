format:
	flake8 src/
	isort src/
	black src/
	ruff check .

run:
	docker compose up --build -d
stop:
	docker compose down
test:
	docker compose exec claim_process python3 -m pytest
