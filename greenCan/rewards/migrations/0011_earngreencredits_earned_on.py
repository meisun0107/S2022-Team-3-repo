# Generated by Django 4.0.2 on 2022-04-24 21:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rewards', '0010_alter_earngreencredits_object_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='earngreencredits',
            name='earned_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
