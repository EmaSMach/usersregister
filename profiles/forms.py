from django.forms import forms
from .models import Users


class UsersForm(forms.Form):
    """
    A form for the Users model.
    """
    class Meta:
        model = Users

        fields = [
            "first_name",
            "last_name",
            "age",
            "gender",
            "email",
            "address",
            "city",
            "state",
            "country",
            "zip_code",
            "phone_number",
            "active",
            "timezone",
        ]

        labels = {
           "first_name": "First Name",
           "last_name": "Last Name",
           "age": "Age",
           "gender": "Gender",
           "email": "Email",
           "address": "Address",
           "city": "City",
           "state": "State",
           "country": "Country",
           "zip_code": "Zip Code",
           "phone_number": "Phone Number",
           "active": "Active",
           "timezone": "Time Zone",
        }
