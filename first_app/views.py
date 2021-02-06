from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

'''
Returns the Hello World Text
'''
def home(request):
    '''
    First Param is for the request Param
    Second param is for the template Param
    Third param is for the data to be returned
    '''
    return render(request, 'home.html', {'name' : 'Simon'})
