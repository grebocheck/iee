"""ieenew URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf  import settings
from django.conf.urls import url
from . import forms
from . import views
from django.views.generic.base import RedirectView
from datetime import datetime
from django.contrib.auth.views import LoginView , LogoutView

urlpatterns = [
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/image/favicon.ico', permanent=True)),
    url(r'^$', views.home, name='home'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^sitemap$' , views.sitemap , name = 'sitemap'),
    path('login/',
         LoginView.as_view
         (
             template_name='login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Вхід',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout', LogoutView.as_view(next_page='/'), name='logout'),
    path('articles/',include('articles.urls')),
    path('events/',include('events.urls')),
    path('profiles/',include('profiles.urls')),
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('^register/$', views.RegisterFormView.as_view( extra_context=
             {
                 'title': 'Реєстрація',
                 'year' : datetime.now().year,
             }))
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(
        settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)