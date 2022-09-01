from django.shortcuts import render
from django.http import HttpResponse
from .models import Tour
# Create your views here.

def index(request):
    context = {
        "tours": Tour.objects.all()
    }
    fileAddy = "static/templates/index.html"
    return render(request, fileAddy, context)