from django.core.validators import ValidationError
import pytz
import re


def validate_first_name(value):
    """Validates the first name."""
    if len(value) <= 3:
        raise ValidationError("First Name should be longer than 3 characters")
    elif len(value) > 3 and value.isdigit():
        raise ValidationError("First Name should not contain numbers only")


def validate_last_name(value):
    """Validate the last name"""
    if len(value) <= 3:
        raise ValidationError("Last Name should be longer than 3 characters")
    elif len(value) > 3 and value.isdigit():
        raise ValidationError("Last Name should not contain numbers only")


def validate_email(email):
    """Checks if email is valid."""
    pattern = re.compile(r"\b[\w.%+-]+@[\w.-]+\.[a-zA-A]{2,6}\b")
    if not re.match(pattern, email):
        raise ValidationError("The email is not valid")


def validate_timezone(timezone):
    """
    Checks if the given timezone is correct.
    """
    if timezone not in pytz.all_timezones:
        raise ValidationError("The Time Zone is not valid")


def validate_city(value):
    """
    Checks if value has a reasonable length.
    """
    if not len(value) >= 4:
        raise ValidationError("Too short")


def validate_state(value):
    """
    Checks if value has a reasonable length.
    """
    if not len(value) >= 4:
        raise ValidationError("Too short")


def validate_country(value):
    """
    Checks if value has a reasonable length.
    """
    if not len(value) >= 4:
        raise ValidationError("Too short")
