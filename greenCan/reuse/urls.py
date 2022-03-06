from django.urls import path

from . import views

app_name = 'reuse'

urlpatterns = [
    path('', views.index, name='index'),
    # URLs here
]