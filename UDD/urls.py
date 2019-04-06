from django.conf.urls import url

from . import views

app_name = "UDD"

urlpatterns = [
    url('', views.index, name='index'),
]
