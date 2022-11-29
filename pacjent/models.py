import datetime

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Patient(models.Model):
    """
        Models:
            Patient - this is user which want get a test result or reservation new test
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pesel = models.CharField(max_length=11, primary_key=True)
    date_of_birth = models.DateField()
    street = models.CharField(max_length=128)
    build_number = models.CharField(max_length=16)
    apartment_number = models.CharField(max_length=16,
                                        null=True)
    post_code = models.CharField(max_length=6)
    city = models.CharField(max_length=128)



TEST = (
    (1, "Badanie krwi"),
    (2, "Badanie moczu"),
)

class TestResultPatient(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    name_test = models.CharField(max_length=128, choices=TEST)
    date_test = models.DateField()
    leukocytes = models.FloatField(null=True) #standard 4.1 - 10.9 #blow
    erythrocytes = models.FloatField(null=True) #standard 3.9-6.5 #blow
    hemoglobin = models.FloatField(null=True) #standard 11.5-17.5 #blow
    hematocrit = models.IntegerField(null=True) #standard 37-52% #blow
    mcv = models.IntegerField(null=True) #standard 80-97 fl #blow
    mch = models.IntegerField(null=True) #standard 26-33 pg #blow
    mchc = models.IntegerField(null=True) #standard 32-36 g/dl #blow
    thrombocytes = models.IntegerField(null=True) #standard 150-450 tys/ul #blow
    rdw = models.FloatField(null=True) #standard 11.5-14.5% #blow
    pdw = models.IntegerField(null=True) #standard 8-13 fl #blow
    plcr = models.IntegerField(null=True) #standard 13-43% #blow
    neutrophils = models.IntegerField(null=True) #standard 50-70% #blow


class Place(models.Model):
    """
        Models:
            Place - place
    """
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128)
    street = models.CharField(max_length=128)
    build_number = models.CharField(max_length=16)
    apartment_number = models.CharField(max_length=16,
                                        null=True)
    post_code = models.CharField(max_length=6)
    city = models.CharField(max_length=128)

"""
    Models:
        Special - all doctor have any special skill
"""
class Special(models.Model):
    name = models.CharField(max_length=128)

"""
    Models:
        Doctor - all doctors which we have in company 
"""
class Doctor(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    special = models.OneToOneField(Special, on_delete=models.CASCADE)

"""
    Models:
        DoctorInPlace:
            doctor : it is a Doctor model
            place : it is a Place model
            date_of_employment : date
"""
class DoctorInPlace(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    date_of_employment = models.DateField(default=datetime.date)

"""
    Models:
        ReservationPatient - this is day when patient reservated new test
"""
class ReservationPatient(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
