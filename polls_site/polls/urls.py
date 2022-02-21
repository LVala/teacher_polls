from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:subject_id>/', views.vote, name='vote'),
    path('<int:subject_id>/recieve_vote/', views.recieve_vote, name='recieve_vote'),
    path('results/', views.results, name='results'),
]