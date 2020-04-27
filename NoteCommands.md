# Commands
	

---
## pip3 install *packages
- => pip3 install django
- => pip3 install djangorestframework

## install packages
- => cd projdemo
- => pip3 freeze > requirements.txt
- install package dependency
- => pip3 install -r requirements.txt

- => pip3 install psycopg2
- => pip3 install psycopg2-binary
- => pip3 install python-decouple

- => pip install django-crontab




---
- check django version
- => django-admin --version


---
- make project
- => django-admin startproject projdemo

---
- make app
- => python3 manage.py startapp home


---
- => python3 manage.py makemigrations
- => python3 manage.py migrate


---
- create super user
- => python3 manage.py createsuperuser