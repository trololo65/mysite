from django.shortcuts import render
from .models import History, Video, Other, Music
from django.views.generic import DetailView


def home(request):
    return render(request, 'home/home.html')


def blago(request):
    return render(request, 'home/blagodarnost.html')


def iris(request):
    return render(request, 'home/iris.html')


def cats(request):
    return render(request, 'home/ocean-cats.html')


def modules(request):
    return render(request, 'home/modules.html')


def music(request):
    music = Music.objects.order_by('-date')
    return render(request, 'home/music.html', {'music': music})


def other(request):
    other = Other.objects.order_by('-date')
    return render(request, 'home/other.html', {'other': other})


def video(request):
    video = Video.objects.order_by('-date')
    return render(request, 'home/video.html', {'video': video})


def history(request):
    history = History.objects.order_by('-date')
    return render(request, 'home/history.html', {'history': history})


class HistoryDetailView(DetailView):
    model = History
    template_name = 'home/detail_view.html'
    context_object_name = 'history'


class OtherDetailView(DetailView):
    model = Other
    template_name = 'home/detail_view_other.html'
    context_object_name = 'other'


class VideoDetailView(DetailView):
    model = Video
    template_name = 'home/detail_view_video.html'
    context_object_name = 'video'

