from django.core.validators import ValidationError
import re


def validate_first_name(value):
    """Validates the first name"""
    if len(value) <= 10:
        raise ValidationError("First Name should be longer than 10 characters")
    elif len(value) > 10 and value.isdigit():
        raise ValidationError("First Name should not contain numbers only")


def validate_last_name(value):
    """Validate the last name"""
    if len(value) <= 10:
        raise ValidationError("Last Name should be longer than 10 characters")
    elif len(value) > 10 and value.isdigit():
        raise ValidationError("Last Name should not contain numbers only")


def validate_email(email):
    """Checks if email is valid."""
    pattern = re.compile(r"\b[\w.%+-]+@[\w.-]+\.[a-zA-A]{2,6}\b")
    if re.match(pattern, email):
        return True
    else:
        raise ValidationError("The email is not valid")
