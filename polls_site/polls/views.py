from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Subject, Choice


def index(request):
    return render(request, 'polls/index.html')

def vote(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    return render(request, 'polls/vote.html', {
        'subject': subject, 
        'range': range(1,11)})

def recieve_vote(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    try:
        context = request.POST
        selected_choice = subject.choice_set.get(teacher_id=int(context['teachers']))
        selected_choice.total_quality += int(context['quality_score'])
        selected_choice.total_friendliness += int(context['friendliness_score'])
        selected_choice.total_motivation += int(context['motivation_score'])
        selected_choice.total_ease += int(context['ease_score'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/vote.html', {
            'subject': subject,
            'range': range(1,11),
            'error_message': "Opcje nie zostały poprawnie zaznaczone",
        })
    else:
        selected_choice.total_voters_number += 1
        selected_choice.save()

        # generate new plots for this subject
        # (preferably asynchronously or on 2nd thread)

        remaining_subjects = Subject.objects.filter(pk__gt=int(subject_id)).order_by('id').all()

        if remaining_subjects:
            return HttpResponseRedirect(reverse('polls:vote', args=(remaining_subjects[0].id,)))
        else:
            return HttpResponseRedirect(reverse('polls:results'))

def results(request):
    return render(request, 'polls/results.html', {'subjects': Subject.objects.all()})
