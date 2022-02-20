from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:subject_id>/', views.vote, name='vote'),
    path('results/', views.results, name='results'),
    path('recive_vote/', views.recive_vote, name='recive_vote'),
]