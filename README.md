### py-blog

1. create a python virtual environment:
    . `python3 -m venv venv`

2. activate virtual environment:
    .  `source/venv/bin/activate`

3. Install requirements.txt 
    .   `pip install -r requirements.txt`

4. migrations:
    . `python manage.py makemigrations`
    . `python manage.py migrate`

5. create superuser:
    . `python manage.py createsuperuser`

6. run the project:
    . `python manage.py runserver`