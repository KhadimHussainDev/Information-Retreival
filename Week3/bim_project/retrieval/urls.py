from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_documents, name='search_documents'),
    path('search-non-overlap/', views.search_non_overlapping_documents, name='search_non_overlap'),
    path('search-proximal-nodes/', views.search_proximal_nodes, name='search_proximal_nodes'),
]
