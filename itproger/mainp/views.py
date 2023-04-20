from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

'''
functions that will be call when user change 'subwebpage'
'''

def index(request):
    data = {
        'title': 'Main ppage',
        'values': ['Some', 'Hello', '123'], 
        'obj': {
            'car': 'BMW',
            'age': 18,
            'hobby': 'Football'
        }   
    }
    return render(request, 'mainp/mainpage.html', data)

def about(request):
    return render(request, 'mainp/aboutus.html')