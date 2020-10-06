from rest_framework import serializers
from . import models
from django.contrib.auth.models import User

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username']

class RatingSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(many=False)
    user = UserSerializer(many=False)
    class Meta:
        model = models.Ratings
        fields = ['id','movie','user','stars']