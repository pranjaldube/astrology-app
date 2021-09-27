# Generated by Django 3.2.3 on 2021-09-27 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astroApp', '0006_auto_20210927_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('httpStatus', models.CharField(max_length=30)),
                ('httpStatusCode', models.IntegerField()),
                ('success', models.BooleanField()),
                ('message', models.CharField(max_length=100)),
                ('apiName', models.CharField(max_length=200)),
                ('data', models.JSONField(blank=True, null=True)),
            ],
        ),
    ]
