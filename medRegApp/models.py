from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from location_field.models.plain import PlainLocationField


# Manager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password=None):
        user = self.create_user(
            email, first_name, last_name, password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


# Models
class CustomUser(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20)
    comment = models.TextField(max_length=500, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Qualification(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Location(models.Model):
    city = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['city'])


class Helper(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)
    qualifications = models.ManyToManyField(Qualification, blank=True)
    medical_leaving_date = models.DateField()
    current_occupation = models.CharField(max_length=100)
    current_medical_occupation = models.BooleanField(default=False)


class Institution(models.Model):
    name = models.CharField(max_length=100)
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    comment = models.TextField(max_length=500, blank=True)


class HelpSeeker(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)


class HelpRequest(models.Model):
    description = models.TextField(max_length=500)
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    required_helper_count = models.IntegerField()
    helpers = models.ManyToManyField(Helper, blank=True)
    help_seeker = models.ForeignKey(HelpSeeker, on_delete=models.CASCADE)
