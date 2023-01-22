import datetime

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
def pesel_validation(pesel):
    """
    :param pesel: Polish id
    :return: information about valid pesel
    """
    if len(pesel) != 11:
        return 1
    elif len(pesel) == 11:
        tab = (1, 3, 7, 9, 1, 3, 7, 9, 1, 3)
        suma = 0
        j = 0
        pesel = list(pesel)
        pesel_list = []
        while j < 11:
            pesel_list.append(int(pesel[j]))
            j += 1
        control_number = (pesel_list[-1])
        i = 0
        while i < len(tab):
            suma += int(pesel_list[i]) * tab[i]
            i += 1

        suma = suma % 10
        if (10 - suma) % 10 != control_number:
            return 1
    return 0

class Patient(models.Model):
    """
        Models:
            Patient - this is user which want get a test result or reservation new test
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pesel = models.CharField(max_length=11)
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
    (3, "Morfologia"),
    (4, "Glukoza"),
    (5, "Próby wątrobowe"),
    (5, "Badanie kreatyny"),
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



class Special(models.Model):
    """
        Models:
            Special - all doctor have any special skill
    """
    name = models.CharField(max_length=128)


class Doctor(models.Model):
    """
        Models:
            Doctor - all doctors which we have in company
    """
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    special = models.OneToOneField(Special, on_delete=models.CASCADE)


class DoctorInPlace(models.Model):
    """
    Models:
        DoctorInPlace:
            doctor : it is a Doctor model
            place : it is a Place model
            date_of_employment : date
    """

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    date_of_employment = models.DateField(default=datetime.date)


class ReservationPatient(models.Model):
    """
        Models:
            ReservationPatient - this is day when patient reservated new test
    """
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
