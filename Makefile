clean:
	rm -rf __pycache__ .pytest_cache
installdeps:
	pip install -r requirements.txt
test:
	pytest tests.py
run:
	python3 pyjokes.py
dockerize:
	docker build -t pyjokes .