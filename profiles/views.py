# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
from .models import Users


def users(request):
    """
    List all the users in database.
    """
    users_lst = Users.objects.all()
    return render(request, 'index.html', {'users_lst': users_lst})


class UsersView(TemplateView):
    template_name = 'users_lst.html'

    def get_context_data(self, **kwargs):
        users = Users.objects.all()
        context = {'users': users}
        return context
