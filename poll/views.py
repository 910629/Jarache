from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
from django.contrib.auth.decorators import login_required


# Create your views here.

def poll(request):
    latest_question_list = Question.objects.all
    context = {'latest_question_list': latest_question_list}
    return render(request, 'poll/poll.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'poll/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'poll/results.html', {'question': question})


@login_required
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    if not request.user.is_authenticated:
        return redirect('user_auth:login')

    try:
        selected_choice = question.choice_set.get(
            pk=request.POST['choice']
        )
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'poll/detail.html', 
            {'question': question,
            'error message': "You didn't select a choice."
        })
    else:
        selected_choice.vote += 1
        selected_choice.save()
        return HttpResponseRedirect(
            reverse('poll:results', args=(question_id,)))