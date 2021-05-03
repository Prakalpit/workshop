from django.db import models

from ckeditor.fields import RichTextField


class Homework(models.Model):
    date=models.CharField(max_length=12,blank=True)
    name=models.CharField(max_length=31,blank=True)
    topic = models.CharField(max_length=12,blank=True)
    url=models.URLField(blank=True)
    description_of_homework = RichTextField(blank=True)



