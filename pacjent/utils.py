from random import sample

import pytz
from faker import Faker

from pacjent.models import Doctor


def fake_data_doctor():
    """Generate fake data for dotor"""
    return {
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "special": faker.special(),
    }
def fake_create_doctor():
    """Create fake doctor"""
    doctor = Doctor.objects.create(**fake_doctor_data())