import os
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.contrib.auth.models import Group 

def send_reminding_mail():
    subject = 'This is a warm welcome.'
    text_body = "we haven't seen you for years! Plz come back"
    from_email = settings.EMAIL_HOST_USER
    g = Group.objects.get(name='mailgroup')
    mailing_list = g.user_set.all()
    bcc = [ v.email for v in mailing_list]
    message = EmailMessage(subject, text_body, from_email, None, bcc) 
    filepath = os.path.join(settings.BASE_DIR, 'images', 'test_image.jpg')
    message.attach_file(filepath)
    message.send()
