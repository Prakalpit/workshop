from django.contrib import admin
from .models import Homework

@admin.register(Homework)

class HomeworkModel(admin.ModelAdmin):
    list_display=('date','name', 'topic')