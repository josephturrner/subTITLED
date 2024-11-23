from django.shortcuts import render, redirect
from .forms import YTMediaForm
from .models import YTMedia
import re

# Create your views here.

def home(request):

    if request.method == 'POST':
        videoInputForm = YTMediaForm(request.POST)
        if videoInputForm.is_valid():
            youtube_url = videoInputForm.cleaned_data['youtube_url']
            video_id = youtube_url.split('v=')[-1]
            video_id = video_id.split('&')[0]
            return render(request, 'home-layout.html', {'videoInputForm': videoInputForm, 'video_id': video_id})

    else:
        videoInputForm = YTMediaForm()


    return render(request, "home-layout.html", {'videoInputForm': videoInputForm})