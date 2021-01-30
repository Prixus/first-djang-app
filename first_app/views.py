from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

'''
Returns the Hello World Text
'''
def home(request):
    return HttpResponse('Hello world')
