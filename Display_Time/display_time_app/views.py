from django.shortcuts import render, HttpResponse
from django.http import response
from time import gmtime, localtime, strftime


def index(request):
    context = { 
        "time": [
            strftime("%Y-%m-%d %H:%M %p", gmtime()),
        ]
        
    }
    return render(request,'index.html', context)