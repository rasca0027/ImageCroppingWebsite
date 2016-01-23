from huey.djhuey import crontab, db_periodic_task
from crop.send_mail import send_reminding_mail

@db_periodic_task(crontab(day='*/2'))
def every_two_days():
    # This is a periodic task that executes queries.
    print 'send another mail!'
    send_reminding_mail()
