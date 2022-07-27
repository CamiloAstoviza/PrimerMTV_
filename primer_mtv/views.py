
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime



def plantilla(request):
    today = datetime.today
    context= {
        'name': ['camilo','ricardo','franco']


    }
    return render(request, 'plantilla.html',context= context)