from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def linking(request):
    return render(request, 'third_app/base.html')

def other(request):
    return render(request, 'third_app/other.html')

def baka(request):
    return render(request, 'third_app/tp.html')