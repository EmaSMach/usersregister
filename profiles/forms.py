from .models import Users, Address
from django import forms
from django.shortcuts import render


class AddressForm(forms.ModelForm):
    """
    A simple form for Address class.
    """
    class Meta:
        model = Address
        fields = ['address']
        labels = {'address': 'Address'}


class UsersForm(forms.ModelForm):
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
           "city": "City",
           "state": "State",
           "country": "Country",
           "zip_code": "Zip Code",
           "phone_number": "Phone Number",
           "active": "Active",
           "timezone": "Time Zone",
        }
