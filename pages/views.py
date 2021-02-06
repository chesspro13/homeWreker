from django.http import HttpResponse
from django.shortcuts import render
import os
# Create your views here.

def home_page(request, *args, **kwargs):

    tab = request.POST.get("ctrl")

    if tab == "play":
        os.system("touch play")  

    if tab == "stop":
        os.system("touch stop")

    print( tab )
    return render(request, "index.html", {})
