# Generated by Django 3.2.3 on 2021-09-26 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AstrologerDetails',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('urlSlug', models.CharField(max_length=200)),
                ('namePrefix', models.CharField(max_length=30)),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('aboutMe', models.CharField(max_length=50)),
                ('profilePicUrl', models.URLField(max_length=300)),
                ('experience', models.FloatField(max_length=30)),
                ('minimumCallDuration', models.FloatField()),
                ('minimumCallDurationCharges', models.FloatField()),
                ('isAvailable', models.BooleanField()),
                ('isOnCall', models.BooleanField()),
            ],
        ),
    ]
