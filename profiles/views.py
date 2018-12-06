# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect, resolve_url, render_to_response
from django.views.generic import TemplateView, DetailView, ListView, CreateView
from django.urls.base import reverse_lazy

# Create your views here.
from .models import Users, Address
from .forms import UsersForm, AddressForm


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


class UsersListView(ListView):
    """
    A class to list all the users.
    """
    model = Users
    template_name = 'users_lst.html'


class UserDetailView(DetailView):
    """
    Show the user details.
    """
    model = Users
    template_name = 'details.html'


class UsersCreateView(CreateView):
    """
    A view to create a new user.
    """
    model = Users
    template_name = 'new.html'
    success_url = reverse_lazy("profiles:simple_lst")

    form_class = UsersForm
    second_form_class = AddressForm

    def get_context_data(self, **kwargs):
        context = super(UsersCreateView, self).get_context_data(**kwargs)
        for i in context:
            print i
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        for i in context:
            print i
        return context

    def post(self, request, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            create_user = form.save(commit=False)
            create_user.address = form2.save()
            create_user.save()
            return HttpResponseRedirect(self.get_success_url())
        else:

            return self.get_context_data()
