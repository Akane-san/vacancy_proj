# Generated by Django 4.1 on 2022-08-31 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vacancy_app", "0007_alter_resume_portfolio"),
    ]

    operations = [
        migrations.AlterField(
            model_name="resume",
            name="portfolio",
            field=models.CharField(max_length=80, null=True),
        ),
    ]
