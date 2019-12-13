from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect


# def home(request):
#     return render(request, 'home.html')

def robots(request):
    return HttpResponse('Hello Wolrd')
