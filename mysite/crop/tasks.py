from huey.djhuey import crontab, db_periodic_task
from crop.send_mail import send_reminding_mail

@db_periodic_task(crontab(minute='*/5'))
def every_four_hours():
    # This is a periodic task that executes queries.
    print 'send another mail!'
    send_reminding_mail()
