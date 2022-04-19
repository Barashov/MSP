from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .models import Data 
# Create your views here.

class Editor(TemplateView):
    template_name = "editor.html"

class Add(View):
    def get(self, request, *args, **kwargs):
        
        text = request.GET["text"]
        photo = request.FILES['file']
        data = Data(text=text, photo=photo)
        data.save()
        return HttpResponse(text)

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request!')

