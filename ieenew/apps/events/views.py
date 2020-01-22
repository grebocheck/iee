from django.http import Http404 , HttpResponseRedirect , HttpResponse
from django.shortcuts import render
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from django.db import models

from .models import Event , Member

def index(request):
    latest_events_list = Event.objects.order_by('-date_post')[:50]
    return render(request , 'events/list.html' , {'latest_events_list': latest_events_list,'title':"Івенти", 'year':datetime.now().year,})

def detail(request , event_id):
    try:
        a = Event.objects.get(id = event_id)
    except:
        raise Http404("Статья не найдена")
    latest_comments_list = a.member_set.order_by('-id')[:10]

    return render(request , "events/detail.html" , {'title':a.title_event,"event": a, 'latest_comments_list': latest_comments_list, 'year':datetime.now().year})


def registr_member(request , event_id ):
    try:
        a = Event.objects.get(id = event_id)
    except:
        raise Http404("Статья не найдена")
    a.member_set.create(name_member = request.POST['name_member'], contact = request.POST['contact'],born_date = request.POST['born_date'],)

    return HttpResponseRedirect(reverse('events:detail' , args = (a.id,)))