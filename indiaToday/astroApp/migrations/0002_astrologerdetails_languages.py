# Generated by Django 3.2.3 on 2021-09-26 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astroApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='astrologerdetails',
            name='languages',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
