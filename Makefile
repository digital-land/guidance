init:
	pip install -r requirements.txt

local:
	python3 render.py --local

fetch/css:
	mkdir -p docs/static/stylesheets
	wget -O docs/static/stylesheets/dl-frontend.css https://raw.githubusercontent.com/digital-land/frontend/master/digital_land_frontend/static/stylesheets/dl-frontend.css

fetch/js:
	mkdir -p docs/static/javascripts/govuk
	wget -O docs/static/javascripts/dl-frontend.js https://raw.githubusercontent.com/digital-land/frontend/master/digital_land_frontend/static/javascripts/dl-frontend.js
	wget -O docs/static/javascripts/dl-cookies.js https://raw.githubusercontent.com/digital-land/frontend/master/digital_land_frontend/static/javascripts/dl-cookies.js
	wget -O docs/static/javascripts/dl-maps.js https://raw.githubusercontent.com/digital-land/frontend/master/digital_land_frontend/static/javascripts/dl-maps.js
	wget -O docs/static/javascripts/govuk/govuk-frontend.min.js https://raw.githubusercontent.com/digital-land/frontend/master/digital_land_frontend/static/javascripts/govuk/govuk-frontend.min.js


fetch: fetch/css fetch/js

render:
	python3 render.py

clobber:
	rm -rf docs/
	mkdir docs