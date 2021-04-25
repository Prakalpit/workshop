from django.shortcuts import render
from .forms import IndividualForm
from .models import Individual

def reg(request):
    form=IndividualForm()
    if request.method=="POST":
        form = IndividualForm(request.POST)
        if form.is_valid():
            form.save()
            form = IndividualForm()

    context={
        'form':form
    }

    return render(request, 'regapp/regfile.html', context)
