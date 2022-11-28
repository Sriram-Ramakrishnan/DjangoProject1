from django.shortcuts import render

# Module for HTTP response
from django.http import HttpResponse

# Below function is added in urls.py for home page
# Sends a HTTP request
def home(request):
    return render(request, 'App1/home.html', {'password': "Abc1235"})

def password(request):
    return render(request, 'App1/password.html', {'password': "Abc1235"})
