from django.db import models
from django.db.models.fields import FloatField
from django.db.models.fields.json import JSONField
# Create your models here.

class AstrologerDetails(models.Model):
    _id= models.AutoField(primary_key=True)
    urlSlug= models.CharField(max_length=200,null=True,blank=True)
    namePrefix = models.CharField(max_length=30,null=True,blank=True)
    firstName= models.CharField(max_length=50)
    lastName= models.CharField(max_length=50,null=True,blank=True)
    aboutMe= models.CharField(max_length=50,)
    profilePicUrl= models.URLField(max_length=300,null=True)
    experience= models.FloatField(max_length=30,null=True,blank=True)
    languages= models.JSONField(null=True,blank=True)
    minimumCallDuration = models.FloatField()
    minimumCallDurationCharges= models.FloatField()
    isAvailable= models.BooleanField()
    rating = FloatField()
    skills= models.JSONField(null=True,blank=True)
    isOnCall= models.BooleanField()
    images = models.JSONField(null=True,blank=True)
    availability= models.JSONField(null=True,blank=True)
    additionalPerMinuteCharges = models.FloatField(max_length=200)
    class Admin:
        pass

class Reports(models.Model):
    _id= models.AutoField(primary_key=True)
    urlSlug= models.CharField(max_length=200,null=True,blank=True)
    namePrefix = models.CharField(max_length=30,null=True,blank=True)
    firstName= models.CharField(max_length=50)
    lastName= models.CharField(max_length=50,null=True,blank=True)
    aboutMe= models.CharField(max_length=50,)
    profilePicUrl= models.URLField(max_length=300,null=True)
    experience= models.FloatField(max_length=30,null=True,blank=True)
    languages= models.JSONField(null=True,blank=True)
    minimumCallDuration = models.FloatField()
    minimumCallDurationCharges= models.FloatField()
    isAvailable= models.BooleanField()
    rating = FloatField()
    skills= models.JSONField(null=True,blank=True)
    isOnCall= models.BooleanField()
    images = models.JSONField(null=True,blank=True)
    availability= models.JSONField(null=True,blank=True)
    additionalPerMinuteCharges = models.FloatField(max_length=200)
    class Admin:
        pass


class BannerOffers(models.Model):
    # _id= models.IntegerField()
    httpStatus= models.CharField(max_length=30)
    httpStatusCode= models.IntegerField()
    success= models.BooleanField()
    message = models.CharField(max_length= 100)
    apiName= models.CharField(max_length=200)
    data= models.JSONField(null=True,blank=True)
    class Admin:
        pass

class Horoscopes(models.Model):
    # _id= models.IntegerField(null=True)
    httpStatus= models.CharField(max_length=30)
    httpStatusCode= models.IntegerField()
    success= models.BooleanField()
    message = models.CharField(max_length= 100)
    apiName= models.CharField(max_length=200)
    data= models.JSONField(null=True,blank=True)
    class Admin:
        pass

class Questions(models.Model):
    # _id= models.IntegerField()
    httpStatus= models.CharField(max_length=30)
    httpStatusCode= models.IntegerField()
    success=models.BooleanField()
    message=models.CharField(max_length=100)
    apiName=models.CharField(max_length=200)
    data= models.JSONField(null=True,blank=True)
    class Admin:
        pass

class Testimonials(models.Model):
    # _id= models.IntegerField()
    httpStatus= models.CharField(max_length=30)
    httpStatusCode= models.IntegerField()
    success=models.BooleanField()
    message=models.CharField(max_length=100)
    apiName=models.CharField(max_length=200)
    data= models.JSONField(null=True,blank=True)
    class Admin:
        pass
