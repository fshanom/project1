from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<title>", views.entry, name="entry"),
    path("wiki", views.index, name="wiki"),
    path('search', views.search, name="search")
]
