from django.shortcuts import render
from .models import VideoAnalysis

def dashboard(request):
    data = VideoAnalysis.objects.all()
    return render(request, 'news_analysis/dashboard.html', {'data': data})
