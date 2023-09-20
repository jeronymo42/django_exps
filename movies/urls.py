from django.urls import path
from movies.views import index

urlpatterns = [
    path('', index),
]
