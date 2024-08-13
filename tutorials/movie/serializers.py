from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.MovieSerializer):
    class Meta:
        model = Movie
        fields = "__all__"