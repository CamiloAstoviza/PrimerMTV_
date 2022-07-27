from multiprocessing import context
from venv import create
from django.shortcuts import render
from family.models import family

def create_person(request):
    new_person = family.objects.create(Name = 'Alex',Lastname ='Astoviza',Age = 19)
    context = {
        'new_person':new_person
    }
    return render(request,'new_person.html',context=context)

def list_family(request):
    Family = family.objects.all()
    context = {
        'Family':Family
    }
    return render(request,'list_family.html',context= context)