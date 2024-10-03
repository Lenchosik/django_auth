from django.urls import re_path
from blog import views

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
]