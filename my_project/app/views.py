from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from django.views import View
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .models import Data 
from .forms import DataForm
# Create your views here.

class Index(TemplateView):
    template_name = "index.html"



class AddView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'editor.html')

    def post(self, request, *args, **kwargs):
        text = request.POST.get("text")
        photo = request.FILES["file"]                       #Book.objects.create
        Data.objects.create(text=text, photo=photo)#
        
        return HttpResponse(text)


