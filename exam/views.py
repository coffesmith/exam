from django.shortcuts import render

# Create your views here.
def index(request)
    return render(request,'index.html')

def myname(request)
    return render(request,'myname.html')