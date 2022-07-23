from django.shortcuts import render

# Create your views here.


def home(request):
    """
    Website homepage. Contains login form if user is not logged in.
    """


def register(request):
    """
    Registration Page.
    """


def blog_post(request, blog_title):
    """
    Page to show the blog contents and comments.
    """


def drafts(request):
    """
    Page that shows a list of drafted blogs awaiting to be published.

    Authors with no admin permission can view only their drafted posts.

    Only authors with admin permissions can view all drafted post.
    """
