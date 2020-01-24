from django.http import Http404 , HttpResponseRedirect , HttpResponse
from django.shortcuts import render
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from django.db import models

from .models import Article , Coment

def index(request):
    latest_articles_list = Article.objects.order_by('-pub_data')[:50]
    return render(request , 'articles/list.html' , {'latest_articles_list': latest_articles_list,'title':"Статті", 'year':datetime.now().year,})

def detail(request , article_id):
    try:
        a = Article.objects.get(id = article_id)
    except:
        raise Http404("Статья не найдена")

    latest_comments_list = a.coment_set.order_by('-id')[:10]

    return render(request , "articles/detail.html" , {"article": a, 'latest_comments_list': latest_comments_list,'title':a.article_title, 'year':datetime.now().year,'author':a.author , 'link_button':a.link_button})

def leave_comment(request , article_id ):
    if request.user.username == "":
        ima = "Невідомий"
    else:
        ima = request.user.username
    try:
        a = Article.objects.get(id = article_id)
    except:
        raise Http404("Статья не найдена")
    a.coment_set.create(author_name = ima, coment_text = request.POST['text'])

    return HttpResponseRedirect(reverse('articles:detail' , args = (a.id,)))
