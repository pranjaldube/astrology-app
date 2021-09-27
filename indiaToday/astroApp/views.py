from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from astroApp.models import AstrologerDetails, BannerOffers, Horoscopes, Questions, Reports, Testimonials
from astroApp.serializers import AstrologerDetailsSerializer, BannerOffersSerializer, HoroscopesSerializer, QuestionsSerializer, ReportsSerializer, TestimonialsSerializer
from django.core.files.storage import default_storage
import requests
# Create your views here.
@api_view(['GET'])
def home(request):
    r1=requests.get('http://127.0.0.1:8000/astro_data').json()
    r2=requests.get('http://127.0.0.1:8000/questions_data').json()
    r3=requests.get('http://127.0.0.1:8000/horoscopes_data').json()
    r4=requests.get('http://127.0.0.1:8000/banneroffers_data').json()
    r5=requests.get('http://127.0.0.1:8000/reports_data').json()
    r6=requests.get('http://127.0.0.1:8000/reports_data').json()

    return JsonResponse({"astro_data": r1, "questions_data": r2, "horoscopes_data": r3, "banneroffers_data": r4, "reports_data": r5, "testimonials_data": r6},safe=False)

@csrf_exempt
def astroApi(request,id=0):
    if request.method=='GET':
        astro_data = AstrologerDetails.objects.all()
        astro_data_serializer=AstrologerDetailsSerializer(astro_data,many=True)
        return JsonResponse(astro_data_serializer.data,safe=False)

    elif request.method=='POST':
        astro=JSONParser().parse(request)
        astro_data_serializer=AstrologerDetailsSerializer(data=astro)
        # print(astro)
        print(astro_data_serializer)
        if astro_data_serializer.is_valid():
            astro_data_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)

    elif request.method=='PUT':
        astro=JSONParser().parse(request)
        astro_data=AstrologerDetails.objects.get(_id=astro['_id'])
        astro_data_serializer=AstrologerDetailsSerializer(astro_data,data=astro)
        if astro_data_serializer.is_valid():
            astro_data_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")

    elif request.method=='DELETE':
        astro_data=AstrologerDetails.objects.get(_id=id)
        astro_data.delete()
        return JsonResponse("Deleted Successfully",safe=False)
# Create your views here.
@csrf_exempt
def reportsApi(request,id=0):
    if request.method=='GET':
        reports_data = Reports.objects.all()
        reports_data_serializer=ReportsSerializer(reports_data,many=True)
        return JsonResponse(reports_data_serializer.data,safe=False)

    elif request.method=='POST':
        reports=JSONParser().parse(request)
        reports_data_serializer=ReportsSerializer(data=reports)
        # print(astro)
        print(reports_data_serializer)
        if reports_data_serializer.is_valid():
            reports_data_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)

    elif request.method=='PUT':
        reports=JSONParser().parse(request)
        reports_data=Reports.objects.get(_id=reports['_id'])
        reports_data_serializer=ReportsSerializer(reports_data,data=reports)
        if reports_data_serializer.is_valid():
            reports_data_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")

    elif request.method=='DELETE':
        reports_data=Reports.objects.get(_id=id)
        reports_data.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def bannersApi(request,id=0):
    if request.method=='GET':
        banneroffers_data = BannerOffers.objects.all()
        banneroffers_data_serializer=BannerOffersSerializer(banneroffers_data,many=True)
        return JsonResponse(banneroffers_data_serializer.data,safe=False)

    elif request.method=='POST':
        banneroffers=JSONParser().parse(request)
        banneroffers_data_serializer=BannerOffersSerializer(data=banneroffers)
        # print(astro)
        print(banneroffers_data_serializer)
        if banneroffers_data_serializer.is_valid():
            banneroffers_data_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)

    elif request.method=='PUT':
        banneroffers=JSONParser().parse(request)
        banneroffers_data=BannerOffers.objects.get(_id=banneroffers['_id'])
        banneroffers_data_serializer=BannerOffersSerializer(banneroffers_data,data=banneroffers)
        if banneroffers_data_serializer.is_valid():
            banneroffers_data_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")

    elif request.method=='DELETE':
        banneroffers_data=BannerOffers.objects.get(_id=id)
        banneroffers_data.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def horoscopesApi(request,id=0):
    if request.method=='GET':
        horoscopes_data = Horoscopes.objects.all()
        horoscopes_data_serializer=HoroscopesSerializer(horoscopes_data,many=True)
        return JsonResponse(horoscopes_data_serializer.data,safe=False)

    elif request.method=='POST':
        horoscopes=JSONParser().parse(request)
        horoscopes_data_serializer=HoroscopesSerializer(data=horoscopes)
        # print(astro)
        # print(astro_data_serializer)
        if horoscopes_data_serializer.is_valid():
            horoscopes_data_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)

    elif request.method=='PUT':
        horoscopes=JSONParser().parse(request)
        horoscopes_data=Horoscopes.objects.get(_id=horoscopes['_id'])
        horoscopes_data_serializer=HoroscopesSerializer(horoscopes_data,data=horoscopes)
        if horoscopes_data_serializer.is_valid():
            horoscopes_data_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")

    elif request.method=='DELETE':
        horoscopes_data=Horoscopes.objects.get(_id=id)
        horoscopes_data.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def questionsApi(request,id=0):
    if request.method=='GET':
        questions_data = Questions.objects.all()
        questions_data_serializer=QuestionsSerializer(questions_data,many=True)
        return JsonResponse(questions_data_serializer.data,safe=False)

    elif request.method=='POST':
        questions=JSONParser().parse(request)
        questions_data_serializer=QuestionsSerializer(data=questions)
        # print(astro)
        # print(astro_data_serializer)
        if questions_data_serializer.is_valid():
            questions_data_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)

    elif request.method=='PUT':
        questions=JSONParser().parse(request)
        questions_data=Questions.objects.get(_id=questions['_id'])
        questions_data_serializer=QuestionsSerializer(questions_data,data=questions)
        if questions_data_serializer.is_valid():
            questions_data_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")

    elif request.method=='DELETE':
        questions_data=Questions.objects.get(_id=id)
        questions_data.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def testimonialsApi(request,id=0):
    if request.method=='GET':
        testimonials_data = Testimonials.objects.all()
        testimonials_data_serializer=TestimonialsSerializer(testimonials_data,many=True)
        return JsonResponse(testimonials_data_serializer.data,safe=False)

    elif request.method=='POST':
        testiomonials=JSONParser().parse(request)
        testimonials_data_serializer=TestimonialsSerializer(data=testiomonials)
        if testimonials_data_serializer.is_valid():
            testimonials_data_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)

    elif request.method=='PUT':
        testimonials=JSONParser().parse(request)
        testimonials_data=Testimonials.objects.get(_id=testimonials['_id'])
        testimonials_data_serializer=TestimonialsSerializer(testimonials_data,data=testimonials)
        if testimonials_data_serializer.is_valid():
            testimonials_data_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")

    elif request.method=='DELETE':
        testimonials_data=Testimonials.objects.get(_id=id)
        testimonials_data.delete()
        return JsonResponse("Deleted Successfully",safe=False)