from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.db.models import ForeignKey

from phonenumber_field.modelfields import PhoneNumberField

from vacancy_proj.settings import BASE_DIR, MEDIA_COMPANY_IMAGE_DIR, MEDIA_SPECIALITY_IMAGE_DIR
import os

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=40)
    logo = models.ImageField(upload_to=MEDIA_COMPANY_IMAGE_DIR)
    description = models.TextField()
    employee_count = models.PositiveIntegerField()
    owner = models.OneToOneField(User, on_delete=models.CASCADE, null=True)


class Specialty(models.Model):
    code = models.SlugField(max_length=20, db_index=True)
    title = models.CharField(max_length=80)
    picture = models.ImageField(upload_to=MEDIA_SPECIALITY_IMAGE_DIR)


class Vacancy(models.Model):
    title = models.CharField(max_length=80)
    specialty = ForeignKey(Specialty, on_delete=models.CASCADE, related_name="vacancies")
    company = ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies")
    skills = models.TextField()
    description = models.TextField()
    salary_min = models.PositiveIntegerField()
    salary_max = models.PositiveIntegerField()
    published_at = models.DateField()


class Application(models.Model):
    written_username = models.CharField(max_length=100)
    written_phone = PhoneNumberField(null = False, blank = False) 
    written_cover_letter = models.TextField()
    vacancy = ForeignKey(Vacancy, on_delete=models.CASCADE, related_name="applications")
    user = ForeignKey(User, on_delete=models.CASCADE, related_name="applications")
