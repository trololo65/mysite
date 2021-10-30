
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('thanks', views.blago, name='thanks'),
    path('history', views.history, name='history'),
    path('iris', views.iris, name='iris'),
    path('music', views.music, name='music'),
    path('modules', views.modules, name='modules'),
    path('cats', views.cats, name='cats'),
    path('video', views.video, name='video'),
    path('other', views.other, name='other'),
    path('history/<int:pk>', views.HistoryDetailView.as_view(), name='history_detail'),
    path('other/<int:pk>', views.OtherDetailView.as_view(), name='other_detail'),
    path('video/<int:pk>', views.VideoDetailView.as_view(), name='video_detail'),
]
