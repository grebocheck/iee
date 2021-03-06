from django.urls import path

from . import views
app_name = 'events'
urlpatterns = [
    path('', views.index , name = 'index'),
    path('<int:event_id>/', views.detail , name = 'detail'),
    path('<int:event_id>/registr_member', views.registr_member , name = 'registr_member'),
]