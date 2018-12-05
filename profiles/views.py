# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView

# Create your views here.
from .models import Users


def users(request):
    """
    List all the users in database.
    """
    users_lst = Users.objects.all()
    return render(request, 'index.html', {'users_lst': users_lst})


class UsersView(TemplateView):
    """
    Shows al the users and their addresses.
    """
    template_name = 'users_lst.html'

    def get_context_data(self, **kwargs):
        users = Users.objects.all()
        context = {'users': users}
        return context


class UserDetailView(DetailView):
    """
    Show the user details.
    """
    model = Users

    def get_context_data(self, request, pk):
        user = get_object_or_404(Users, pk)
        context = {'user': user}
        if user:
            return render(request, 'details.html', context)
