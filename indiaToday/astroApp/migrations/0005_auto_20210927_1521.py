# Generated by Django 3.2.3 on 2021-09-27 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astroApp', '0004_astrologerdetails_additionalperminutecharges'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerOffers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('httpStatus', models.CharField(max_length=30)),
                ('httpStatusCode', models.IntegerField(max_length=30)),
                ('success', models.BooleanField()),
                ('message', models.CharField(max_length=100)),
                ('apiName', models.CharField(max_length=200)),
                ('data', models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Horoscopes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('httpStatus', models.CharField(max_length=30)),
                ('httpStatusCode', models.IntegerField(max_length=30)),
                ('success', models.BooleanField()),
                ('message', models.CharField(max_length=100)),
                ('apiName', models.CharField(max_length=200)),
                ('data', models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('httpStatus', models.CharField(max_length=30)),
                ('httpStatusCode', models.IntegerField(max_length=30)),
                ('success', models.BooleanField()),
                ('message', models.CharField(max_length=100)),
                ('apiName', models.CharField(max_length=200)),
                ('data', models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('urlSlug', models.CharField(blank=True, max_length=200, null=True)),
                ('namePrefix', models.CharField(blank=True, max_length=30, null=True)),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(blank=True, max_length=50, null=True)),
                ('aboutMe', models.CharField(max_length=50)),
                ('profilePicUrl', models.URLField(max_length=300, null=True)),
                ('experience', models.FloatField(blank=True, max_length=30, null=True)),
                ('languages', models.JSONField(blank=True, null=True)),
                ('minimumCallDuration', models.FloatField()),
                ('minimumCallDurationCharges', models.FloatField()),
                ('isAvailable', models.BooleanField()),
                ('rating', models.FloatField()),
                ('skills', models.JSONField(blank=True, null=True)),
                ('isOnCall', models.BooleanField()),
                ('images', models.JSONField(blank=True, null=True)),
                ('availability', models.JSONField(blank=True, null=True)),
                ('additionalPerMinuteCharges', models.FloatField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='astrologerdetails',
            name='experience',
            field=models.FloatField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='astrologerdetails',
            name='lastName',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='astrologerdetails',
            name='namePrefix',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='astrologerdetails',
            name='profilePicUrl',
            field=models.URLField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='astrologerdetails',
            name='urlSlug',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
