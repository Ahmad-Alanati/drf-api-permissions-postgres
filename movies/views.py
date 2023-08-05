from django.shortcuts import render
from .models import Movie
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView
from .serializers import MovieSerializer,MovieCreateSerializer

# Create your views here.
class MovieListView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetailView(RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieCreateView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieCreateSerializer

class MovieUpdateView(RetrieveUpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDeleteView(RetrieveDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieAllView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer