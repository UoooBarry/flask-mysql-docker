init:
	python3 -m pip install -r ./app/requirements.txt
up:
	docker-compose up --build