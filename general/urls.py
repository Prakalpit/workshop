from django.urls import path
from .views import index, syllabus
urlpatterns=[
    path("", index, name="home"),
    path("syllabus/", syllabus, name="syllabus"),
]