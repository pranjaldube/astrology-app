# Generated by Django 3.2.3 on 2021-09-27 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astroApp', '0005_auto_20210927_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banneroffers',
            name='httpStatusCode',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='horoscopes',
            name='httpStatusCode',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='questions',
            name='httpStatusCode',
            field=models.IntegerField(),
        ),
    ]
