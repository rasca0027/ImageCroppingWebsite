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
If you do not want to refresh, just want to load new, use:

    python manage.py load_data


## Run Server

    python manage.py runserver


## Manual

To change default money value for cropping jobs,  
change the amount in `crop/views.py`, on line 74 (for cropping) and line 100 (for no crop).  

To login to superuser, do `python manage.py createsuperuser` and login to `localhost:8000/admin`.  


## Change A New DB

just replace your pkl file.  
Then run:

    python manage.py load_data

This command will check DB and will not update values.


## Dump DB to report

    python manage.py report

This will create a pkl file in project directory named `report.pkl`.
