
from djongo import models
from django.contrib.auth.models import AbstractUser
from djongo.models import ObjectIdField

class Team(models.Model):
    id = ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class User(AbstractUser):
    id = ObjectIdField(primary_key=True, editable=False)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, db_column='team_id', to_field='id')

class Activity(models.Model):
    id = ObjectIdField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id', to_field='id')
    type = models.CharField(max_length=50)
    duration = models.IntegerField()  # in minutes
    distance = models.FloatField()    # in kilometers
    def __str__(self):
        return f"{self.user.username} - {self.type}"

class Workout(models.Model):
    id = ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()  # in minutes
    def __str__(self):
        return self.name

class Leaderboard(models.Model):
    id = ObjectIdField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id', to_field='id')
    points = models.IntegerField()
    def __str__(self):
        return f"{self.user.username} - {self.points}"
