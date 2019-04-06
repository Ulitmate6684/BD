from django.urls import path

from . import views

app_name = "UDD"

urlpatterns = [
    path('', views.index, name='index'),
]
