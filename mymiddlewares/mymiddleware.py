# A simple middleware to check if the user email is an @gmail one.
from django.contrib.auth.models import User
from django.contrib.auth import get_user
from django.shortcuts import redirect
from django.core.validators import ValidationError
import re


def is_gmail_email(email):
    """
    Check if the email is a gmail one.
    """
    pattern = re.compile(r"\b[\w.%+-]+@gmail.com\b")
    if not re.match(pattern, email):
        raise ValidationError("The email is not valid")


class MyMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        if request.user.is_authenticated():
            print "Email", request.user.email
            print "Email from POST", request.POST.get('email')
            print "Email from GET", request.GET.get('email')
            try:
                print is_gmail_email(request.user.email)
            except ValidationError:
                redirect('http://www.google.com')
            except TypeError:
                print "Ponga un usuario."


            # user = get_user(request)
            # print dir(user), "USUARIO", type(user), user.is_authenticated(), user.email
            # if request.method == "GET":
            #     if request.GET.get('email'):
            #         try:
            #             is_gmail_email(request.GET.get('email'))
            #         except ValidationError:
            #             redirect('http://www.google.com')
            #     else:
            #         if request.user.is_authenticated():
            #             try:
            #                 is_gmail_email(request.user.get('email'))
            #             except ValidationError:
            #                 redirect('http://www.google.com')

        # Code to be executed for each request/response after
        # the view is called.

        return response