from django.urls import path
from . import views

urlpatterns = [
    path('interference/', views.interference_model_view, name='interference'),
    path('belief/', views.belief_network_view, name='belief'),
]
