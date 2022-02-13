from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[path('',views.project,name='project'),path("predict",views.predict,name='Predictions')]


