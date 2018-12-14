Link: http://142.93.64.24

## Installation

create directory media
```bash
mkdir media
```

Create a virtual environment
```bash
python -m venv env
```

Activate virtual environment
```bash
source env/Scripts/activate
```

Install all packages
```bash
pip install -r requirements.txt
```
Apply migration
```bash
python manage.py migrate
```

Create superuser
```bash
python manage.py createsuperuser
```

## Docker
```bash
git clone 
mkdir media AND docker/logs
add app/conf.py
docker
```
