from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class AccountView(TemplateView):
    template_name = 'accounts/accounts.html'


class RegisterView(TemplateView):
    template_name = 'accounts/register.html'