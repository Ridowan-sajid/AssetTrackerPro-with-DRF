# Generated by Django 4.2.4 on 2023-08-24 15:58

import Asset.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
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
                ("company_code", models.CharField(max_length=20, unique=True)),
                ("title", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="GadgetUser",
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
                ("name", models.CharField(max_length=20)),
                (
                    "phone",
                    models.CharField(
                        max_length=11,
                        validators=[Asset.models.validate_phone_number_length],
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                (
                    "profile_picture",
                    models.ImageField(
                        blank=True, null=True, upload_to=Asset.models.custom_image_name
                    ),
                ),
                (
                    "company",
                    models.ForeignKey(
                        editable=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Asset.company",
                    ),
                ),
            ],
        ),
    ]
