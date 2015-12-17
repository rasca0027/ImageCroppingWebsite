# Readme

## Set Up Environment

    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt

## Initialize

    python manage.py migrate
    python manage.py init_data

!! warning !!
If you do it, all the data will be refresh.

## Run Server

    python manage.py runserver 
