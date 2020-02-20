from django.shortcuts import render
from django.http import HttpResponse
from . import forms

# Create your views here.

def index(request):
    return HttpResponse('<em>Second App</em>')

def form_name_view(request):
    form = forms.FormName()

    if(request.method == 'POST'):
        form = forms.FormName(request.POST)

        if(form.is_valid()):
            print("Validation SUCCESS")
            print("NAME:"+form.cleaned_data['name'])
            print("EMAIL:"+form.cleaned_data['email'])
            print("TEXT:"+form.cleaned_data['text'])

    return render(request, 'second_app/form_page.html', {'form':form})