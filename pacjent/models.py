import datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


def check_post_code(value):
    pass


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pesel = models.CharField(max_length=11)
    date_of_birth = models.DateField()
    street = models.CharField(max_length=128)
    build_number = models.CharField(max_length=16)
    apartment_number = models.CharField(max_length=16,
                                        null=True,
                                        default=None)
    post_code = models.CharField(max_length=6, validators=[check_post_code])
    city = models.CharField(max_length=128)


class Place(models.Model):
    pass


class Special(models.Model):
    name = models.CharField(max_length=128)


class Doctor(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    special = models.OneToOneField(Special, on_delete=models.CASCADE)
    date_of_employment = models.DateField(default=datetime.date)


class DoctorInPlace(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)



