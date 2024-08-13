from rest_framework import serializers
from .models import Movie

class MovieSerializers(serializers.MovieSerializers):
    class Meta:
        model = Movie
        fields = "__all__"