from django.urls import path
from django.contrib import admin
from . import  views
urlpatterns = [
    path('stuinfo/<int:pk>',views.student_detail),
    path('stuinfo/',views.student_list),
]
