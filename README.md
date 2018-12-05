Link: http://138.197.107.116

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
