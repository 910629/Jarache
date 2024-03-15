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

    :Args:  request: An HTTP request object.
            question_id: The primary key (pk) of the question to retrieve.

    :Returns: An HTTP response with the rendered poll/detail.html template containing
        the details of the specified question.
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'poll/detail.html', {'question': question})


def results(request, question_id):
    """This function renders the results page for a specific question,
    by retrieving a question from the database based on the provided
    question ID (`question_id`) and presenting its associated results on a webpage
    using the 'poll/results.html' template. If the question with the given ID
    is not found, an HTTP 404 (Not Found) error response is raised.

    :Args:  request: An HTTP request object.
            question_id: The primary key (pk) of the question to retrieve (assumed to be an integer).

    :Returns: An HTTP response object with the rendered poll/results.html template
        containing the results for the requested question.

    :Raises: Http404: If the question with the given ID is not found in the database.
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'poll/results.html', {'question': question})


@login_required
def vote(request, question_id):
    """Records a vote for a specific choice within a question.
    It handles user votes on a question. It first retrieves the
    question based on the provided ID (`question_id`) and verifies if the user
    is authenticated using the `@login_required` decorator. If not authenticated,
    it redirects the user to the login page.

    The function then attempts to retrieve the selected choice based on the
    submitted form data (`request.POST['choice']`). If the choice ID is missing
    or the choice doesn't exist, it renders the detail template (`poll/detail.html`)
    with an error message.

    On successful retrieval of the selected choice, the function increments its
    `vote` count, saves the changes, and redirects the user to the results page
    for the specific question using `HttpResponseRedirect` and `reverse`.

    :Args:  request: An HTTP request object.
            question_id: The primary key (pk) of the question to vote on (assumed to be an integer).

    :Returns:   An HTTP response object:
                - Redirects to the login page if the user is not authenticated.
                - Renders the detail template with an error message if the choice is invalid.
                - Redirects to the results page for the question upon successful vote.
    :Raises Http404: If the question with the given ID is not found (indirectly through get_object_or_404).
    """
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