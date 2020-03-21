MedReg
======

# Installation
* `pip install -r requirements.txt`
* `python manage.py migrate`
# Load Data into Database

* `python manage.py loaddata ./seed/fixture.json` 
* Use `fixtureMaker.py` if you added new qualifications to `qualifications.txt` to create new `fixture.json`.