from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
class Movie(models.Model):
    movie_name = models.CharField(max_length=120, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    
    @property
    def no_of_ratings(self):
        ratings = Ratings.objects.filter(movie=self)
        return len(ratings)

    @property
    def avg_rating(self):
        sum = 0
        ratings = Ratings.objects.filter(movie=self)
        for rating in ratings:
            sum += rating.stars
        if len(ratings) > 0:
            return sum / len(ratings)
        else:
            return 0

class Ratings(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movies')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    class Meta:
        unique_together = (('movie','user'),)
        index_together = (('movie','user'),)