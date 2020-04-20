from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView, ListView, View, DetailView
from account.models import User, Profile as Pro
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from account.forms import ProfileEdit


@method_decorator(login_required(login_url='/login'), name='dispatch')
class Profile(DetailView):
    template_name = 'profile.html'
    queryset = User.objects.filter(is_active=True)
    fields = ('id', 'first_name', 'last_name')
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['profile'] = Pro.objects.filter(user_id__exact=self.queryset.first().id).first()

        return context


@method_decorator(login_required(login_url='/login'), name='dispatch')
class ProfileEdit(UpdateView):
    template_name = 'profile-edit.html'
    queryset = User.objects.filter(is_active=True)
    form_class = ProfileEdit
    success_url = reverse_lazy('home')

