from django.urls import path
from app.views import Editor

urlpatterns = [
    
    path("editor/", Editor.as_view(), name="app"),
]

