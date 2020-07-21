from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def web(request):
    return render(request,"myweb/web.html")
def regs(request):
    fname =request.POST['fn']
    lname =request.POST["ln"]
    email=request.POST["email"]
    phNo=request.POST["phoneNo"]
    s=open("lgr.txt",'a')


    s.write(fname+","+lname+","+phNo+","+email+"\n")

    s.close()

    return render(request,"myweb/form.html")
    