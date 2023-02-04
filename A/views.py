from django.shortcuts import render
from rest_framework import viewsets
from .models import Person
from .serializers import PersonSerializer
from . import models
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

def index(request):
    context={}
    return render(request, 'index.html', context)

def upload(request):
    if request.method=='POST':
        Person_Name=request.POST.get('name'),
        District_Name=request.POST.get('dis'),
        FIRNo=request.POST.get('fir'),
        age=request.POST.get('age'),
        Gender=request.POST.get('gender'),
        FIR_Date=request.POST.get('date'),
        image = request.FILES['image'],
        Photo_Full_front=str(image)
        print(Photo_Full_front)
        if image:
            print(image)
            # encodings = face_recognition.face_encodings(image)[0]
            # print(encodings)
            pass
        print(Person_Name,District_Name,FIRNo,age,Gender,FIR_Date,Photo_Full_front)

    context={

    }
    return render(request,'upload.html',context)

def vni(request):
    context={}
    return render(request, 'vni.html', context)
