# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView, DetailView, ListView, CreateView
from django.urls.base import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
from .models import Users
from .forms import UsersForm, AddressForm


@login_required
def users(request):
    """
    List all the users stored in the database.
    """
    users_lst = Users.objects.all()
    return render(request, 'profiles/users.html', {'users_lst': users_lst})


# This is what the exercise asked for, however,
# I used the UsersListView(ListView) instead.
# If you want to use it, just UserListView by UsersView
# in the urls.py of this django app (profiles)
@method_decorator(login_required, name='dispatch')
class UsersView(TemplateView):
    """
    Shows all the users and their addresses.
    """
    template_name = 'profiles/users_lst.html'

    def get_context_data(self, **kwargs):
        users = Users.objects.all()
        context = {'object_list': users}
        return context


@method_decorator(login_required, name='dispatch')
class UsersListView(ListView):
    """
    A class to list all the users.
    """
    model = Users
    template_name = 'profiles/users_lst.html'


@method_decorator(login_required, name='dispatch')
class UserDetailView(DetailView):
    """
    Show the user details.
    """
    model = Users
    template_name = 'profiles/details.html'


@method_decorator(login_required, name='dispatch')
class UsersCreateView(CreateView):
    """
    A view to create a new user.
    """
    model = Users
    template_name = 'profiles/new.html'
    success_url = reverse_lazy("profiles:new")

    form_class = UsersForm
    second_form_class = AddressForm

    def get_context_data(self, **kwargs):
        context = super(UsersCreateView, self).get_context_data(**kwargs)
        if 'users_form' not in context:
            context['users_form'] = self.form_class(self.request.GET)
        if 'address_form' not in context:
            context['address_form'] = self.second_form_class(self.request.GET)
        return context

    def post(self, request, **kwargs):
        self.object = self.get_object
        users_form = self.form_class(request.POST)
        address_form = self.second_form_class(request.POST)
        if users_form.is_valid() and address_form.is_valid():
            create_user = users_form.save(commit=False)
            create_user.address = address_form.save()
            create_user.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(context={'users_form': users_form,
                                                    'address_form': address_form})
