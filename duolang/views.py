from django.shortcuts import render

def home(request):
    return render(request, 'duolang/home.html')

def greeting(request):
    return render(request, 'duolang/greeting.html')    