from django.http import HttpResponse
from django.shortcuts import render



# Create your views here.
def home_view(request,*args,**kwrgs):
    print(args,kwrgs)
    return render(request,"home.html",{})

def contact_view(*args,**kwrgs):
    return HttpResponse("<h1>Contact Page</h1>")