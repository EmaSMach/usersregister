"""
A simple middleware to check if the user email is an @gmail one.
"""
from django.shortcuts import redirect
from django.core.validators import ValidationError
from django.contrib.auth import logout
import re


def is_gmail_email(email):
    """
    Check if the email is a gmail one.
    """
    pattern = re.compile(r"\b[\w.%+-]+@gmail.com\b")
    if not re.match(pattern, email):
        raise ValidationError("The email is not a gmail address")


class MyMiddleware(object):
    """
    Checks if the email of the logged user is a gmail account.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        """
        The code that will be executed.
        """
        response = self.get_response(request)
        if request.user.is_authenticated() and not request.user.is_superuser:
            try:
                is_gmail_email(request.user.email)
            except ValidationError:
                logout(request)
                return redirect('login')
            except TypeError:
                print "An error occurred"
                return redirect('login')
        return response
