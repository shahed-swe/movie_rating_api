from django.shortcuts import render
from rest_framework import viewsets, status
from . import models
from . import serializers
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer
    authentication_classes = (TokenAuthentication, )
    # permission_classes = (IsAuthenticated, )

    # this things are for giving message to front-end
    @action(detail=True, methods=['POST'])
    def rate_movie(self, request,pk=None):
        print(request.data)
        if 'stars' in request.data:
            movie = models.Movie.objects.get(id=pk)
            print("Movie Title", movie.movie_name)
            response = {'message': 'its working'}
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'message':"it's not working"}
            return Response(response, status=status.HTTP_404_NOT_FOUND)

class RatingViewSet(viewsets.ModelViewSet):
    queryset = models.Ratings.objects.all()
    serializer_class = serializers.RatingSerializer