# Generated by Django 4.1 on 2022-08-28 18:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("vacancy_app", "0003_alter_vacancy_published_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="company",
            name="owner",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="company",
            name="logo",
            field=models.ImageField(upload_to="company_images"),
        ),
        migrations.AlterField(
            model_name="specialty",
            name="picture",
            field=models.ImageField(upload_to="speciality_images"),
        ),
        migrations.CreateModel(
            name="Application",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("written_username", models.CharField(max_length=100)),
                (
                    "written_phone",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None, unique=True
                    ),
                ),
                ("written_cover_letter", models.TextField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="applications",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "vacancy",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="applications",
                        to="vacancy_app.vacancy",
                    ),
                ),
            ],
        ),
    ]