from django.db import models
from ckeditor.fields import RichTextField

class Individual(models.Model):
    name=models.CharField(max_length=23)
    mail=models.EmailField(blank=False)
    phone=models.CharField(max_length=10)
    message=RichTextField(blank=True, null=True)


    def __str__(self):
        return self.name