from django.urls import path
from app.views import AddView, Index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", Index.as_view(), name="app"),
    path("editor/", AddView.as_view(), name="app"),
    path("add/", AddView.as_view(), name="app"),


    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)