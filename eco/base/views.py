from django.shortcuts import render, redirect
from . forms import VideoForm


# Create your views here.
def home(request):
    return render(request, 'home.html')

def upload(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('postupload')
    else:
            form = VideoForm()
    return render(request, 'upload.html', {'form' : form})

def postupload(request):
    return render(request, 'postupload.html')
