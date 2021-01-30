from django.urls import path
from . import views

'''
Creates all the routes for our app
'''
urlpatterns = [
    path('', views.home, name='home')
]
