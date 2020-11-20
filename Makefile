init:
	pip install -r requirements.txt

render:
	python3 render.py

clobber:
	rm -rf docs/
	mkdir docs