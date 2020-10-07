from django.shortcuts import render
from rest_framework import viewsets, status
from . import models
from . import serializers
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer



class MovieViewSet(viewsets.ModelViewSet):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    # this things are for giving message to front-end
    @action(detail=True, methods=['POST'])
    def rate_movie(self, request,pk=None):
        if 'stars' in request.data:
            movie = models.Movie.objects.get(id=pk)
            stars = int(request.data['stars'])
            response = {'message':'not done yet'}
            try:
                if stars >= 1 and stars <= 5:
                    rating = models.Ratings.objects.get(user=request.user, movie=movie.id)
                    rating.stars = stars
                    rating.save()
                    serializer = serializers.RatingSerializer(rating, many=False)
                    response = {'message': 'Rating Updated','result':serializer.data}
                    return Response(response, status=status.HTTP_200_OK)
                else:
                    response = {'message':'number is not in the range'}
                    return Response(response, status=status.HTTP_204_NO_CONTENT)
            except:
                rating = models.Ratings.objects.create(user=request.user, movie=movie, stars=stars)
                serializer = serializers.RatingSerializer(rating, many=False)
                response = {'message':'Rating Created','result':serializer.data}
                return Response(response, status=status.HTTP_201_CREATED)
        else:
            response = {'message':"it's not working"}
            return Response(response, status=status.HTTP_404_NOT_FOUND)

class RatingViewSet(viewsets.ModelViewSet):
    queryset = models.Ratings.objects.all()
    serializer_class = serializers.RatingSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)