from django.db import models
from django.db.models import ForeignKey


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=40)
    logo = models.URLField(default='https://place-hold.it/100x60')
    description = models.TextField()
    employee_count = models.PositiveIntegerField()


class Specialty(models.Model):
    code = models.SlugField(max_length=20, db_index=True)
    title = models.CharField(max_length=80)
    picture = models.URLField(default='https://place-hold.it/100x60')


class Vacancy(models.Model):
    title = models.CharField(max_length=80)
    specialty = ForeignKey(Specialty, on_delete=models.CASCADE, related_name="vacancies")
    company = ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies")
    skills = models.TextField()
    description = models.TextField()
    salary_min = models.PositiveIntegerField()
    salary_max = models.PositiveIntegerField()
    published_at = models.DateField()
