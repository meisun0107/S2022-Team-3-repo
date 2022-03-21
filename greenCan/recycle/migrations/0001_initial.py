# Generated by Django 4.0.2 on 2022-03-21 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ZipCode",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("zip_code", models.CharField(max_length=5)),
                ("state_id", models.CharField(max_length=2)),
                ("state", models.CharField(max_length=100)),
                ("borough", models.CharField(max_length=13)),
                ("centroid_latitude", models.FloatField()),
                ("centroid_longitude", models.FloatField()),
                ("polygon", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="DropOffLocation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(max_length=250)),
                ("latitude", models.FloatField()),
                ("longitude", models.FloatField()),
                ("items_accepted", models.TextField(null=True)),
                ("type", models.CharField(max_length=250)),
                ("public_email", models.EmailField(max_length=254, null=True)),
                ("phone_number", models.CharField(max_length=17, null=True)),
                ("street_address", models.TextField()),
                (
                    "zip_code",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="recycle.zipcode",
                    ),
                ),
            ],
        ),
    ]
