from django.urls import path
from . import views

app_name = 'jay_profile'
urlpatterns = [
    path('', views.index, name='index'),
    path('store', views.store, name='store'),
]