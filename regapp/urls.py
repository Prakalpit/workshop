from django.urls import path
from .views import reg

urlpatterns=[
    path("", reg, name="regfile"),
]