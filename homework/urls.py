from django.urls import path
from .views import homework
urlpatterns=[
    path("submission/",homework, name="hw"),
]