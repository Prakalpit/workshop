from django.shortcuts import render
from .forms import HomeworkForm
def homework(request):
    form=HomeworkForm()
    form = HomeworkForm(request.POST)
    if form.is_valid():
        form.save()
        form = HomeworkForm()
    context = {
        'form': form
    }

    return render(request, 'homework/hw_upload_file.html', context)
