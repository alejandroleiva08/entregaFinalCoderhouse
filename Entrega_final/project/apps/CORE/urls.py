from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import views

app_name = "CORE"

urlpatterns = [
    path('',views.home, name="home"),
]

urlpatterns += staticfiles_urlpatterns()