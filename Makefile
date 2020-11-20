init:
	pip install -r requirements.txt

local:
	python3 render.py --local

render:
	python3 render.py

clobber:
	rm -rf docs/
	mkdir docs