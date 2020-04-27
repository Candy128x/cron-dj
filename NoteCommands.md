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


**Note**
- => python manage.py crontab add
- => python manage.py crontab show
- => python manage.py crontab remove
- => crontab -e
- => crontab -l


(venv) ashish@ashish-Vostro-3478:.../cron-dj$ /media/ashish/UBUNTU/var/www/html/py-proj/django/cron-dj/venv/bin/python3 /media/ashish/UBUNTU/var/www/html/py-proj/django/cron-dj/projdemo/manage.py crontab run 5dee6bc62b0f0ddb483d004736463f34
---Hello-cron-job---

- => python3 manage.py shell < apple/cron.py


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