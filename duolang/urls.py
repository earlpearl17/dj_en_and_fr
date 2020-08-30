from django.urls import path

from . import views

app_name = 'duolang'

urlpatterns = [
    path('', views.home, name='home'),
    path('greeting/', views.greeting, name='greeting'),
]