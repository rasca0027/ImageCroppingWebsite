# Readme

## Set Up Environment

    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt

If encounter problems, try `sudo apt-get install libjpeg-dev` and install again.

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


## Send Email

First, set email account at bottom of `mysite/settings.py`  

Second, modify mailing list.  
There are two ways:  
1. Manually login to `admin` page and create a group named `mailgroup`.  And then add the users to that group.  
2. Edit the file `crop/management/commands/create_mailgroup.py`. Add the username to the list `mailing list` and save. And then run `python manage.py create_mailgroup`.

Third, log in to your gmail account here: https://support.google.com/mail/answer/14257?hl=zh-Hant  
and change settings of 允許安全性較低的應用程式存取您的帳戶.  

Fourth, start the hue server.  

** You are all done! **
