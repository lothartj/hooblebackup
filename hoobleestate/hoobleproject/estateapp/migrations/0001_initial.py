# Generated by Django 4.1.13 on 2024-04-23 12:38

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ContactAgent",
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
                ("user_name", models.CharField(max_length=100)),
                ("surname", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("mobile_number", models.CharField(max_length=15)),
                ("message", models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name="Listing",
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
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("title", models.CharField(max_length=255)),
                ("location", models.CharField(max_length=100)),
                ("erf_size", models.DecimalField(decimal_places=2, max_digits=6)),
                ("description", models.TextField()),
                ("bedroom_count", models.IntegerField()),
                ("bathroom_count", models.IntegerField()),
                ("lounge_size", models.CharField(max_length=100)),
                ("tv_room", models.CharField(max_length=100)),
                ("dining_area", models.CharField(max_length=100)),
                ("kitchen_description", models.TextField()),
                ("entertainment_area", models.TextField()),
                ("additional_amenities", models.TextField()),
                ("outdoor_features", models.TextField()),
                ("agent_email", models.EmailField(max_length=254)),
                ("agent_contact_number", models.CharField(max_length=20)),
                ("iframe_url", models.URLField()),
            ],
        ),
    ]
