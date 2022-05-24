from django.db import models

# Create your models here.
class Series(models.Model):
  HORROR = 'horror'
  COMEDY = 'comedy'
  ACTION = 'action'
  DRAMA = 'drama'
  
  CATEGORIES_CHOICES = {
    (HORROR, 'Horror'),
    (COMEDY, 'Comedy'),
    (ACTION, 'Action'),
    (DRAMA, 'Drama'),
  }
  
  name = models.CharField(max_length=100)
  release_date = models.DateField()
  raiting = models.IntegerField(default=0)
  category = models.CharField(max_length=10, choices=CATEGORIES_CHOICES)
  
  def __str__(self):
    return