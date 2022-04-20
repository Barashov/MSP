from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .models import Data 

# Create your views here.





class AddView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'editor.html')

    def post(self, request, *args, **kwargs):
        text = request.POST.get("text")
        photo = request.FILES["file"]                       #Book.objects.create
        Data.objects.create(text=text, photo=photo)#
        
        return redirect("/")


class Index(ListView):
    model = Data
    context_object_name = 'object'
    template_name='index.html'
