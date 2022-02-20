from multiprocessing import context
from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Subject, Teacher, Choice

from django.http import HttpResponse


def index(request):
    return render(request, 'polls/index.html')

def results(request):
    response = "You're looking at the results of question"
    return HttpResponse(response)

def vote(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    return render(request, 'polls/vote.html', {'subject': subject})

def recive_vote(request):
    pass
