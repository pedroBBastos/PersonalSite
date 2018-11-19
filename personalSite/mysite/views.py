from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'mysite/index.html', {})

def unicamp(request):
    return render(request, 'mysite/unicamp.html', {})

def hacklife(request):
    return render(request, 'mysite/hackLife.html', {})
