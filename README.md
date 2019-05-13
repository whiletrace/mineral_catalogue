# Mineral Catalogue [![Build Status](https://travis-ci.com/whiletrace/Python_Proj6.svg?branch=master)](https://travis-ci.com/whiletrace/Python_Proj6)
## summary
This is a django built dynamic app that displays minerals and there attributes, current mineral attributes displayed: 
* name
* image filename
* image caption
* category
* formula
* strunz classification
* color
* crystal system
* unit cell
* crystal symmetry
* cleavage
* mohs scale hardness
* luster
* streak
* diaphaneity
* optical properties
* refractive index
* crystal habit
* specific gravity

data can be found at ./data/minerals.json 
data is outputted minerals list pg 
and minerals detail pg
 ###built on:
 
 **sufficient to run locallay**
 * python  3.5
 * django  2.1.7
 * pytz 2018.2
 
 **additionally included for heroku deployment**
 * dj-database-url 0.5.0
 * gunicorn 19.9.0
 * psycopg2-binary 2.8.1
 * whitenoise 4.1.2
 
 ## to run locally:
 * clone repo and cd to root dir
 * suggested that you run virtualenv
 * pip install -r requirements.txt** within shell
 
 ###create db tables and migrate data
 *  run **python manage.py makemigrations**
 *  run **python manage.py migrate** 
 
 ### start server
 *  run **python manage.py runserver 8000**
 ## to run tests:
 ** run manage.py tests