from django.db import models
from django.db.models import ForeignKey
from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField

from vacancy_proj.settings import MEDIA_COMPANY_IMAGE_DIR, MEDIA_SPECIALITY_IMAGE_DIR


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
    written_phone = PhoneNumberField(null=False, blank=False)
    written_cover_letter = models.TextField()
    vacancy = ForeignKey(Vacancy, on_delete=models.CASCADE, related_name="applications")
    user = ForeignKey(User, on_delete=models.CASCADE, related_name="applications")


class Resume(models.Model):
    class GradeType(models.TextChoices):
        intern = 'Стажер'
        junior = 'Джуниор'
        middle = 'Миддл'
        senior = 'Синьор'
        lead = 'Лид'

    class StatusType(models.TextChoices):
        chill = 'Не ищу работу'
        review = 'Рассматриваю предложения'
        search = 'Ищу работу'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=40)
    status = models.CharField(max_length=25, choices=StatusType.choices)
    salary = models.PositiveIntegerField()
    specialty = ForeignKey(Specialty, on_delete=models.CASCADE, related_name="resumes")
    grade = models.CharField(max_length=7, choices=GradeType.choices)
    education = models.TextField()
    experience = models.TextField()
    portfolio = models.CharField(max_length=80, null=True)
