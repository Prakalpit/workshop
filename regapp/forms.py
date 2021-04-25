from django.forms import ModelForm
from .models import Individual

class IndividualForm(ModelForm):
    class Meta:
        model=Individual
        fields="__all__"




