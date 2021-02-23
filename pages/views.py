from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from youtube_dl import YoutubeDL
import subprocess
import os
import time
import pafy

nextTime = 0
lastTime = 0


def home_page(request, *args, **kwargs):
    tab = request.POST.get("ctrl")

    print("Mils: " + str(getLengthMills()))

    context = {
        'length': getLength(),
        'mills': getLengthMills()
    }

    try:
        print("Tab: " + tab)
    except:
        print("Tab: None")

    if tab == "play":
        print("Play")
        os.system("touch /speaker/commands/play")  

    if tab == "stop":
        print("Pause")
        os.system("touch /speaker/commands/stop")

    if tab == "volumeUp":
        print("Volume up")
        os.system("touch /speaker/commands/volumeUp")

    if tab == "volumeDown":
        print("Volume down")
        os.system("touch /speaker/commands/volumeDown")

    return render(request, "index.html", context)


def base_page(request, *args, **kwargs):
    return render(request, "base.html", {})


def scroll_testing(request, *args, **kwargs):
    return render(request, "scrollTesting.html", {})


def volumeUp(request, *args, **kwargs):
    os.system("touch /speaker/commands/volumeUp")
    return HttpResponse("Done")


def volumeDown(request, *args, **kwargs):
    os.system("touch /speaker/commands/volumeDown")
    return HttpResponse("Done")


def play(request, *args, **kwargs):
    os.system("touch /speaker/commands/play")
    return HttpResponse("Done")


def pause(request, *args, **kwargs):
    os.system("touch /speaker/commands/stop")
    return HttpResponse("Done")


def rewind(request, *args, **kwargs):
    os.system("touch /speaker/commands/rewind")
    return HttpResponse("Done")


def forward(request, *args, **kwargs):
    os.system("touch /speaker/commands/forward")
    return HttpResponse("Done")


def restart(request, *args, **kwargs):
    os.system("touch /speaker/commands/restart")
    return HttpResponse("Done")


@csrf_exempt
def playSong(request, *args, **kwargs):
    d = request.POST

    print( '\n\n\nGonna play ' + d['song'] + "\n\n\n")

    return HttpResponse("Done")

def getCurTime(request, *args, **kwargs):
    os.system("touch /speaker/commands/getTime")
    print("Waiting for the client to get me the current time")
    while os.path.isfile("/speaker/commands/curTime") == False:
        time.sleep(0.001)
    print("Yay! The server responded with the time!")
    print("Got the current time")
    f = open("/speaker/commands/curTime", "r")
    s = f.read()
    f.close()
    print("I have the time at " + s)
    os.system("rm /speaker/commands/curTime")
    return HttpResponse(str(s))


def curPos(request, *args, **kwargs):
    global nextTime
    global lastTime

    # if nextTime > 0:
#  if time.time()*1000 > nextTime:
    if os.path.isfile("/speaker/commands/curTime"):
        f = open("/speaker/commands/curTime", 'r')
        s = f.read()
        f.close()
        return HttpResponse(str(s))
#   return HttpResponse( str( lastTime))


def getLengthMills():
    if os.path.isfile("/speaker/commands/audioLength"):
        f = open("/speaker/commands/audioLength", 'r')
        s = f.read()
        f.close()
        return s


def getLength():
    if os.path.isfile("/speaker/commands/audioLength"):
        f = open("/speaker/commands/audioLength", 'r')
        s = f.read()
        f.close()
        # print( "Length: " + str(type(s)) + str(s))
        l = time.gmtime(int(s)/1000)
        return time.strftime("%H:%M:%S", l)


def downloadPage(request, *args, **kwargs):
    return render(request, "downloader.html", {})


@csrf_exempt
def downloadAudio(request, *args, **kwargs):
    url = "https://www.youtube.com/watch?v=OlWomZbCW6I"
    url = request.POST.get('url')
    url = request.body

    f = open("/speaker/commands/downloadThis", 'w')
    f.write(url.decode('utf-8'))
    f.close()
    print("Downloading audio for " + str(url.decode('utf-8')))
    # subprocess.run(['youtube-dl', '--extract-audio', '--audio-format', 'mp3', '-o', '/speaker/songs/%(title)s.%(ext)s', url])
    # subprocess.run(['rm', '/speaker/songs/%(title)s.webm'])
    return HttpResponse("Copy")


# TODO: Use this to optimise stuff
def checkInit():
    if os.path.isfile("/speaker/commands/init") != False:
        print("There is a user connecting for the first time")
