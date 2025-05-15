from django.shortcuts import render
from .models import VideoAnalysis
from django.shortcuts import render
from .forms import YouTubeURLForm
from .utils.sentiment_utils import analyze_sentiment

def dashboard(request):
    data = VideoAnalysis.objects.all()
    return render(request, 'news_analysis/dashboard.html', {'data': data})


def analyze_video(request):
    context = {}
    if request.method == 'POST':
        form = YouTubeURLForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            # Write logic here
            context['url'] = url
            context['analysis'] = {'title': 'Demo Title', 'bias': 'Neutral'}  # placeholder
    else:
        form = YouTubeURLForm()

    context['form'] = form
    return render(request, 'news_analysis/analyze.html', context)