from django.http import HttpResponse
from django.shortcuts import render
import os
import time
# Create your views here.

def home_page(request, *args, **kwargs):
    tab = request.POST.get("ctrl")

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

def volumeDown(request, *args, **kwargs):
    os.system("touch /home/pi/commands/volumeDown")

def play(request, *args, **kwargs):
    os.system("touch /home/pi/commands/play")

def pause(request, *args, **kwargs):
    os.system("touch /home/pi/commands/stop")

def getCurTime(request, *args, **kwargs):
    os.system("touch /home/pi/commands/getTime")
    while os.path.isfile("/home/pi/commands/time") == False:
        time.sleep(0.01)
    f = open("/home/pi/commands/time","r")
    s = f.read()
    print( "I have the time at " + s )
    f.close()
    os.system("rm /home/pi/commands/time")
    return HttpResponse( str(s))


def curPos(request, *args, **kwargs):
    global nextTime
    global lastTime

    #f nextTime > 0:
#  if time.time()*1000 > nextTime:
    f = open("/home/pi/commands/curTime", 'r')
    s = f.read()
    f.close()
    print( s )
    return HttpResponse(str(s))
#   return HttpResponse( str( lastTime))

def getLengthMills():
    f = open("/home/pi/commands/audioLength",'r')
    s = f.read()
    f.close()
    return s

def getLength():
    f = open("/home/pi/commands/audioLength",'r')
    s = f.read()
    f.close()
    print( "Length: " + str(type(s)) + str(s))
    l = time.gmtime(int(s)/1000)
    return time.strftime("%H:%M:%S", l)
