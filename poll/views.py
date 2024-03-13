from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
from django.contrib.auth.decorators import login_required


# Create your views here.

def poll(request):
    """This function renders the poll listing page for the application, 
    by retrieving all available questions from the database and presents them on a webpage.

    :Args request: An HTTP request object.

    :Returns: An HTTP response with the rendered poll/poll.html template containing a
        list of all questions.
    """
    latest_question_list = Question.objects.all
    context = {'latest_question_list': latest_question_list}
    return render(request, 'poll/poll.html', context)


def detail(request, question_id):
    """ This function renders the detail page for a specific question,
    by retrieving a question from the database based on the provided
    question ID (`question_id`) and presenting it on a webpage. It utilizes
    `get_object_or_404` to handle the case where the question ID is not found,
    raising a 404 HTTP status code (page not found) in that scenario.

    Args:
        request: An HTTP request object.
        question_id: The primary key (pk) of the question to retrieve.

    Returns:
        An HTTP response with the rendered poll/detail.html template containing
        the details of the specified question.
    """
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