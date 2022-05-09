# Generated by Django 4.0.2 on 2022-05-08 01:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0008_alter_volunteerapplication_score"),
    ]

    operations = [
        migrations.AlterField(
            model_name="volunteerapplication",
            name="approved_by",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reviewer",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]