from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from youtube_dl import YoutubeDL
import subprocess
import os
import time
import pafy
# Create your views here.

def home_page(request, *args, **kwargs):
    tab = request.POST.get("ctrl")

    print( "Mils: " + str(getLengthMills() ))

    context = {
        'length': getLength(),
        'mills': getLengthMills()
    }

    

    try:
        print( "Tab: " + tab)
    except:
        print("Tab: None")

    if tab == "play":
        print( "Play")
        os.system("touch /home/pi/commands/play")  

    if tab == "stop":
        print( "Pause")
        os.system("touch /home/pi/commands/stop")

    if tab == "volumeUp":
        print("Volume up")
        os.system("touch /home/pi/commands/volumeUp")

    if tab == "volumeDown":
        print("Volume down")
        os.system("touch /home/pi/commands/volumeDown")


    return render(request, "index.html", context)

nextTime = 0
lastTime = 0

def volumeUp(request, *args, **kwargs):
    os.system("touch /home/pi/commands/volumeUp")
    return HttpResponse( "Done")

def volumeDown(request, *args, **kwargs):
    os.system("touch /home/pi/commands/volumeDown")
    return HttpResponse( "Done")

def play(request, *args, **kwargs):
    os.system("touch /home/pi/commands/play")
    return HttpResponse( "Done")

def pause(request, *args, **kwargs):
    os.system("touch /home/pi/commands/stop")
    return HttpResponse( "Done")

def rewind(request, *args, **kwargs):
    os.system("touch /home/pi/commands/rewind")
    return HttpResponse( "Done")

def forward(request, *args, **kwargs):
    os.system("touch /home/pi/commands/forward")
    return HttpResponse( "Done")

def restart(request, *args, **kwargs):
    os.system("touch /home/pi/commands/restart")
    return HttpResponse( "Done")

def getCurTime(request, *args, **kwargs):
    os.system("touch /home/pi/commands/getTime")
    print("Waiting for the client to get me the current time")
    while os.path.isfile("/home/pi/commands/curTime") == False:
        time.sleep(0.001)
    print("Yay! The server responded with the time!")
    print("Got the current time")
    f = open("/home/pi/commands/curTime","r")
    s = f.read()
    f.close()
    print( "I have the time at " + s )
    os.system("rm /home/pi/commands/curTime")
    return HttpResponse( str(s))


def curPos(request, *args, **kwargs):
    global nextTime
    global lastTime

    #f nextTime > 0:
#  if time.time()*1000 > nextTime:
    if os.path.isfile("/home/pi/commands/curTime"):
        f = open("/home/pi/commands/curTime", 'r')
        s = f.read()
        f.close()
        return HttpResponse(str(s))
#   return HttpResponse( str( lastTime))

def getLengthMills():
    if os.path.isfile("/home/pi/commands/audioLength"):
        f = open("/home/pi/commands/audioLength",'r')
        s = f.read()
        f.close()
        return s

def getLength():
    if os.path.isfile("/home/pi/commands/audioLength"):
        f = open("/home/pi/commands/audioLength",'r')
        s = f.read()
        f.close()
        #print( "Length: " + str(type(s)) + str(s))
        l = time.gmtime(int(s)/1000)
        return time.strftime("%H:%M:%S", l)

def downloadPage(request, *args, **kwargs):
    return render(request, "downloader.html", {})

@csrf_exempt
def downloadAudio( request, *args, **kwargs ):
    url = "https://www.youtube.com/watch?v=OlWomZbCW6I"
    url = request.POST.get('url')
    print("Downloading audio for " + type(url) )
    subprocess.run(['youtube-dl', '--extract-audio', '--audio-format', 'mp3', '-o', '/home/pi/songs/%(title)s.%(ext)s', url])
    subprocess.run(['rm', '/home/pi/songs/%(title)s.webm'])
