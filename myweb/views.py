from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def web(request):
    return render(request,"myweb/web.html")

    