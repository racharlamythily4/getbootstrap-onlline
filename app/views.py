from django.shortcuts import render

# Create your views here.

def boot1(request):
    return render(request,'boot1.html')

def button(request):
    return render(request,'button.html')

def alert(request):
    return render(request,'alert.html')

def badge(request):
    return render(request,'badge.html')