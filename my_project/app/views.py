from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponse

# Create your views here.

class Editor(TemplateView):
    template_name = "editor.html"


