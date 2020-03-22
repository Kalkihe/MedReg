MedReg
======

# Installation
* `pip install -r requirements.txt`
* `python manage.py migrate`
* `python manage.py compilemessages --locale de`

# Load Data into Database
* `python manage.py loaddata ./seed/fixture.json` 
* Use `fixtureMaker.py` if you added new qualifications to `qualifications.txt` to create new `fixture.json`.

# Sending mails
Following these instructions enables invite mails when adding helpers to a help request.

Setup your mail server connection in `MedReg/settings.py`:
```
EMAIL = True
EMAIL_HOST = '<smtp host>'
EMAIL_PORT = <smtp port>
EMAIL_HOST_USER = '<stmp user>'
EMAIL_HOST_PASSWORD = '<stmp password>'
EMAIL_USE_TLS = <whether mail server uses tls>
```
[Django documentation on sending mails](https://docs.djangoproject.com/en/3.0/topics/email/)
