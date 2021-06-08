from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .tasks import my_task
def index(request):
    my_task.delay(10)
    return HttpResponse('<h1> my_task done</h1>')
