from django.http import HttpResponse
from django.shortcuts import render
import os
import time
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

def volumeDown(request, *args, **kwargs):
    os.system("touch /home/pi/commands/volumeDown")

def play(request, *args, **kwargs):
    os.system("touch /home/pi/commands/play")

def pause(request, *args, **kwargs):
    os.system("touch /home/pi/commands/stop")

def getCurTime(request, *args, **kwargs):
    os.system("sudo touch /home/pi/commands/getTime")
    print("Waiting for the client to get me the current time")
    while os.path.isfile("/home/pi/commands/curTime") == False:
        time.sleep(0.01)
    print("Got the current time")
    f = open("/home/pi/commands/curTime","r")
    s = f.read()
    print( "I have the time at " + s )
    f.close()
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
        print( "Length: " + str(type(s)) + str(s))
        l = time.gmtime(int(s)/1000)
        return time.strftime("%H:%M:%S", l)
