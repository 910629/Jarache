from django.shortcuts import render

# Create your views here.
def index(request):
    """This method renders the index page for the application.

    :Args request: An HTTP request object.

    :Returns: An HTTP response with the rendered index.html template.
    """
    return render(request, 'index.html')


def store(request):
    """This method renders the store page for the application.

    :Args request: An HTTP request object.

    :Returns: An HTTP response with the rendered store.html template.
    """
    return render(request, 'store.html')



