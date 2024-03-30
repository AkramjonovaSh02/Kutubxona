
from django.contrib import admin
from django.urls import path

from mainApp_3.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', add_muallif, name='add_muallif'),
    path('add2/', add_record, name='add_record'),
    path('add3/', add_kutubxonachi)
]