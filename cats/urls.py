from .views import CatView
from django.urls import path

urlpatterns = [path("cats/", CatView.as_view())]

