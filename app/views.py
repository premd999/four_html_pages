from django.shortcuts import render

# Create your views here.

def pushpa(request):
    return render(request, 'pushpa.html')

def macha(request):
    return render(request,'macha.html')

def rollex(request):
    return render(request, 'rollex.html')

def bigil(request):
    return render(request,'bigil.html')