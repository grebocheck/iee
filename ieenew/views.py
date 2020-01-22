from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from profiles.models import Profile
from articles.models import Article
from events.models import Event

class RegisterFormView(FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/login/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    latest_articles_list = Article.objects.order_by('-pub_data')[:25]
    latest_events_list = Event.objects.order_by('-date_post')[:25]

    aaat = 0
    bbbt = 0

    #print(str(latest_articles_list[0].pub_data))
    #print(str(datetime.date(latest_articles_list[aaat].pub_data)))
    #print(str((latest_events_list[bbbt].date_post)))

    html = []

    for a in range(10):
        a += 1
        try:
            try:
                latest_events_list[bbbt]
            except IndexError:
                html.append(latest_events_list[bbbt])
                aaat +=1
                continue
            try:
                latest_articles_list[aaat]
            except IndexError:
                html.append(latest_events_list[bbbt])
                bbbt += 1 
                continue
            if latest_events_list[bbbt].date_post > latest_articles_list[aaat].pub_data:
                html.append(latest_events_list[bbbt])
                bbbt +=1
            else:
                html.append(latest_articles_list[aaat])
                aaat += 1  
        except:
            pass

    return render(request,'index.html',{'latest_events_list':latest_events_list,'latest_articles_list':latest_articles_list,'html': html,'title':'Головна','year':datetime.now().year,})

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'contact.html',
        {
            'title':'Контакти',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )


def sitemap(request):
    """Renders the sitemap page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'sitemap.xml',
        {
            'title':'Плани на сайт',
            'message':'Heridium site description',
            'year':datetime.now().year,
        }
    )

    sponseRedirect(reverse('articles:detail' , args = (a.id,)))

