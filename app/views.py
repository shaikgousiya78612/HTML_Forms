from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_Topic(request):
    if request.method=='POST':
        tn=request.POST['topic']
        t=Topic.objects.get_or_create(topic_name=tn)[0]
        t.save()
        return HttpResponse('insert_Topic is done succussfully')
    return render(request,'insert_Topic.html')


def insert_webpage(request):
    ts=Topic.objects.all()
    d={'ts':ts}

    if request.method=='POST':
        topic=request.POST['topic']
        na=request.POST['na']
        ur=request.POST['ur']
        T=Topic.objects.get_or_create(topic_name=topic)[0]
        T.save()
        W=Webpage.objects.get_or_create(topic_name=T,name=na,url=ur)[0]
        W.save()
        return HttpResponse('Webpage is inserted succussfully')
    
    return render(request,'insert_webpage.html',d)

def insert_ar(request):
    AO=Webpage.objects.all()
    d={'AO':AO}

    if request.method=='POST':
        topic=request.POST['topic']
        na=request.POST['na']
        ur=request.POST['ur']
        da=request.POST['da']
        T=Topic.objects.get_or_create(topic_name=topic)[0]
        T.save()
        W=Webpage.objects.get_or_create(topic_name=T,name=na,url=ur)[0]
        W.save()
        A=AccessRecords.objects.get_or_create(name=W,date=da)[0]
        A.save()
        return HttpResponse('AccessRecord is inserted succussfully')

        
        
    return render(request,'insert_ar.html',d)