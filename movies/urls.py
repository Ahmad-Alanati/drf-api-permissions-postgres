from django.urls import path
from .views import MovieListView,MovieDetailView,MovieCreateView,MovieUpdateView,MovieDeleteView,MovieAllView

urlpatterns = [
    path('',MovieListView.as_view(), name = 'movie_list'),
    path('<int:pk>/',MovieDetailView.as_view(), name = 'movie_detail'),
    path('create/',MovieCreateView.as_view(), name = 'movie_create'),
    path('<int:pk>/update/',MovieUpdateView.as_view(), name = 'movie_update'),
    path('<int:pk>/delete/',MovieDeleteView.as_view(), name = 'movie_delete'),
    path('<int:pk>/all/',MovieAllView.as_view(), name = 'movie_all'),
]