import os

# create dir media and logs
os.system('mkdir media')
os.system('mkdir docker/logs')

# create and start project
os.system('python3 -m venv env && '
          'source env/bin/activate && '
          'pip install -r requirements.txt &&'
          'python manage.py migrate &&'
          'python manage.py createsuperuser &&'
          'python manage.py runserver')

