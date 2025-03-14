from django.urls import path
from . import views

urlpatterns = [
    path('ai-agent', views.index, name='apis-index'),
]
