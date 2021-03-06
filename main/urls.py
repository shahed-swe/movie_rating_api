from django.urls import path
from rest_framework import routers
from django.conf.urls import include 
from . import views

router = routers.DefaultRouter()
router.register(r'movie',views.MovieViewSet)
router.register(r'ratings',views.RatingViewSet)
router.register(r'user', views.UserViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
