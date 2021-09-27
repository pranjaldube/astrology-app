from rest_framework import serializers
from astroApp.models import AstrologerDetails, BannerOffers, Horoscopes, Questions, Reports, Testimonials

class AstrologerDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AstrologerDetails
        fields=('_id','urlSlug','namePrefix','firstName','rating','lastName','skills','availability','images','aboutMe','languages','profilePicUrl','experience','minimumCallDuration','minimumCallDurationCharges','isAvailable','isOnCall','additionalPerMinuteCharges')

class ReportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reports
        fields=('_id','urlSlug','namePrefix','firstName','rating','lastName','skills','availability','images','aboutMe','languages','profilePicUrl','experience','minimumCallDuration','minimumCallDurationCharges','isAvailable','isOnCall','additionalPerMinuteCharges')

class BannerOffersSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerOffers
        fields=('httpStatus','httpStatusCode','success','message','apiName','data')

class HoroscopesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horoscopes
        fields=('httpStatus','httpStatusCode','success','message','apiName','data')

class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields=('httpStatus','httpStatusCode','success','message','apiName','data') 

class TestimonialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonials
        fields=('httpStatus','httpStatusCode','success','message','apiName','data') 