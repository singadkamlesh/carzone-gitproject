from django.urls import path
from . import views
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from django.views.static import serve

urlpatterns = [
path('',views.home,name='home'),
path('about',views.about,name='about'),
path('services',views.services,name='services'),
#path('cars',views.cars,name='cars'),
path('contact',views.contact,name='contact')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
