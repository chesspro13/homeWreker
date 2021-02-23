"""HomeWreker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pages.views import home_page, curPos, pause, play, volumeUp, volumeDown, getCurTime
from pages.views import downloadPage, downloadAudio, rewind, forward, restart, base_page
from pages.views import scroll_testing, playSong

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('curPos', curPos),
    path('pause', pause),
    path('play', play),
    path('volumeUp', volumeUp),
    path('volumeDown',volumeDown),
    path('getTime', getCurTime),
    path('download', downloadPage),
    path('downloadAudio', downloadAudio),
    path('rewind', rewind),
    path('forward', forward),
    path('restart', restart),
    path('testing', base_page),
    path('scrollTesting', scroll_testing),
    path('playSong', playSong),
]
