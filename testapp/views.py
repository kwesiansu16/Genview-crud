from django.shortcuts import render
from django.views.generic.edit import CreateView
from  django.views.generic.list import ListView
from  django.views.generic.detail import DetailView
from .models import Registration


# Create your views here.
class RegistrationCreate(CreateView):
    model = Registration
    fields = ['fname','lname','city','email']
    success_url='/'

class RegistrationList(ListView):
    model = Registration

class RegistrationDetail(DetailView):
    model = Registration