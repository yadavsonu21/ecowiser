from django.shortcuts import render, redirect
from . forms import VideoForm
import subprocess
from pathlib import Path

# Create your views here.
def home(request):
    return render(request, 'home.html')


def upload(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            # import subprocess

            BASE_DIR = Path(__file__).resolve().parent.parent
            ccext_loc = f'C:\Program Files (x86)\CCextractor\ccextractor'
            # command = '8849331ddae9c3169024d569ce17b9a4fdd917401cd6c6bfb8dc1fd59c6af21e.mp4'
            cdd = str(BASE_DIR) + '/videos/' + "8849331ddae9c3169024d569ce17b9a4fdd917401cd6c6bfb8dc1fd59c6af21e.mp4  -o outputvids"
            subprocess.run(ccext_loc + ' ' + cdd)

            form.save()
            return redirect('postupload')
    else:
            form = VideoForm()
    return render(request, 'upload.html', {'form' : form})

def postupload(request):
    return render(request, 'postupload.html')
