from django.core.mail import send_mass_mail
from django.shortcuts import reverse
from django.conf import settings


def send_invite_mail(hr, helpers):
    messages = map(
        lambda h: (
            'Neue Einladung zu einem Hilfegesuch',
            f'''Hallo {h.user.first_name} {h.user.last_name},

du wurdest zu einem Hilfegesuch eingeladen:
Zuständige Institution: {hr.help_seeker.institution}
Zeitraum: {hr.start_date} bis {hr.end_date}
Weitere Details: {reverse('help_request_detail', args=(hr.id,))}

Informationen zum Hilfesuchenden:
E-Mail: {hr.help_seeker.user.email}
Telefonnummer: {hr.help_seeker.user.phone_number}

Mit freundlichen Grüßen,
    MedReg Team
            ''',
            settings.EMAIL_HOST_USER,
            (h.user.email,)
        ),
        helpers
    )
    send_mass_mail(tuple(messages), fail_silently=False)
