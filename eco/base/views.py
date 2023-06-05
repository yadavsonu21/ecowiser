from django.shortcuts import render, redirect
from . forms import VideoForm
from . models import Subtitle
import subprocess
from pathlib import Path

# Create your views here.
BASE_DIR = Path(__file__).resolve().parent.parent
def home(request):
    return render(request, 'home.html')

def srt_to_pg(srt_file):

    with open(srt_file, 'r') as f:
        content = f.read()

    subtitle_entries = content.strip().split('\n\n')

    for i, subtitle_entry in enumerate(subtitle_entries):

        if not subtitle_entry[0].isdigit():
            continue

        lines = subtitle_entry.split('\n')
        id = int(lines[0])
        timestamp = lines[1]
        phrase = ' '.join(lines[2:])

        subtitle = Subtitle(entry_id = id, timestamp_vid= timestamp, phrase_vid=phrase)
        subtitle.save()
def upload(request):
    if request.method == 'POST':


        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():

            # import subprocess
            f_name = request.FILES['video_file'].name
            # video_file = request.FILES
            # video_file = Video.video_file
            # file = request.FILES['videofile']
            # temp = form.video_file
            form.save()
            video_path = str(BASE_DIR) + '/videos/' + f_name
            output_dir = r'C:\Users\xmate\PycharmProjects\eco\eco\Outputvids'
            ccext_loc = r'C:\Program Files (x86)\CCextractor\ccextractor'
            command = f' "{ccext_loc}" "{video_path}" -o "{output_dir}"'
            subprocess.run(command, shell=True)
            srt_to_pg(output_dir)


            return redirect('postupload')
    else:
            form = VideoForm()
    return render(request, 'upload.html', {'form' : form})

def postupload(request):

    return render(request, 'postupload.html')
