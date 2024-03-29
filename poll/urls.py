from django.urls import path
from . import views

app_name = 'poll'
urlpatterns = [
    path('poll', views.poll, name='poll'),
    path('<int:question_id>', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]