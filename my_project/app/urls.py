from django.urls import path
from app.views import Editor, Add

urlpatterns = [
    
    path("editor/", Editor.as_view(), name="app"),
    path("add/", Add.as_view(), name="app")
]

