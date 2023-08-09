from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['name','price','description','released_date']

class MovieCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id','name','purchaser','price','description','released_date']