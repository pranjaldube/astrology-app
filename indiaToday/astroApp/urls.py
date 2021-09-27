from django.conf.urls import url
from astroApp import views
from django.urls import path, re_path


urlpatterns=[
    url(r'^home',views.home),
    url(r'^astro_data$',views.astroApi),
    url(r'^astro_data/([0-9]+)$',views.astroApi),
    url(r'^questions_data$',views.questionsApi),
    url(r'^questions_data/([0-9]+)$',views.questionsApi),
    url(r'^horoscopes_data$',views.horoscopesApi),
    url(r'^horoscopes_data/([0-9]+)$',views.horoscopesApi),
    url(r'^banneroffers_data$',views.bannersApi),
    url(r'^banneroffers_data/([0-9]+)$',views.bannersApi),
    url(r'^reports_data$',views.reportsApi),
    url(r'^reports_data/([0-9]+)$',views.reportsApi),
     url(r'^testimonials_data$',views.testimonialsApi),
    url(r'^testimonials_data/([0-9]+)$',views.testimonialsApi)
]