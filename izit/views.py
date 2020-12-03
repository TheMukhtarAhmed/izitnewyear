from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def home(request):
    now = datetime.datetime.now()
    return render(request, 'izit/home.html', {
        "newyear" : now.month == 1 and now.day == 1,
    })