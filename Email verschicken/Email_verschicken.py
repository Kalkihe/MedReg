from django.core.mail import send_mail

send_mail('subject','Content','Absender email',['Empfänger email'],fail_silently=False,)

# Email server in settings.py einfügen