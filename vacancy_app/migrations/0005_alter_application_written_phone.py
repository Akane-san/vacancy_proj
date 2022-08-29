# Generated by Django 4.1 on 2022-08-29 13:32

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ("vacancy_app", "0004_company_owner_alter_company_logo_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="application",
            name="written_phone",
            field=phonenumber_field.modelfields.PhoneNumberField(
                max_length=128, region=None
            ),
        ),
    ]
