from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class LogOutPage(TemplateView):
    template_name = 'exit.html'

class HomePage(TemplateView):
    template_name = 'index.html'

class AboutView(TemplateView):
    template_name = 'about.html'