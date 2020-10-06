from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
class Movie(models.Model):
    movie_name = models.CharField(max_length=120, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)

class Ratings(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movies')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    class Meta:
        unique_together = (('movie','user'),)
        index_together = (('movie','user'),)