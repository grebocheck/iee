from django.shortcuts import render
from django.http import Http404 , HttpResponseRedirect , HttpResponse
from django.shortcuts import render
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from django.db import models
from ieenew.forms import UserForm , ProfileForm
from django.contrib import messages
from django.shortcuts import redirect

from .models import Profile
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST,request.FILES, instance=request.user)
        profile_form = ProfileForm(request.POST,request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Ваш профиль был успешно обновлен!'))
            return  render(request, 'profile.html', {
                    'user_form': user_form,
                    'profile_form': profile_form
                })
        else:
            messages.error(request, ('Пожалуйста, исправьте ошибки.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })