from django.urls import path
from hello_word import views

urlpatterns = [
    path('', views.hello_word, name='hello_word'),
]