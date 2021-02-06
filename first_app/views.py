from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

'''
Returns the Hello World Text
'''
def home(request):
<<<<<<< HEAD
    return HttpResponse('Hello world')
=======
    '''
    First Param is for the request Param
    Second param is for the template Param
    Third param is for the data to be returned
    '''
    return render(request, 'home.html', {'name' : 'Simon'})
>>>>>>> 65a265139b5493f9a6a9c0c6a9154e4f387d8b68
