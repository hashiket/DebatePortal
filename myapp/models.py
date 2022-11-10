from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UsersType(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    USER_TYPE_CHOICES = (
      ("admin", 'Admin'),
      ("Mod", 'Moderator'),
      ("abu", 'AdminBus'),
     )

    user_type = models.CharField(choices=USER_TYPE_CHOICES,max_length=25)
    userstatus = models.BooleanField(default=True)

class DebateTopic(models.Model):
    topic_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    aduser = models.ForeignKey(User, on_delete = models.CASCADE)
    closestatus = models.BooleanField(default=False)

class Views(models.Model):
    view_id = models.AutoField(primary_key=True)
    topic = models.ForeignKey(DebateTopic, on_delete = models.CASCADE)
    user = models.ManyToManyField(DebateTopic)
    description = models.CharField(max_length=100)

class Votes(models.Model):
    vote_id = models.AutoField(primary_key=True)
    user = models.ForeignField(User, on_delete = models.CASCADE)
    view = models.ForeignField(Views, on_delete = models.CASCADE)
    topic = models.ForeignField(DepateTopic, on_delete = models.CASCADE)
    votestatus = models.BooleanField()

class DepateWinner(models.Model):
    dw_id = models.AutoField(primary_key=True)
    user = models.ForeignField(User, on_delete = models.CASCADE)
    topic = models.ForeignField(DepateTopic, on_delete = models.CASCADE)
    winstatus = models.BooleanField()

class TopicSuggest(models.Model):
    user = models.ForeignField(User, on_delete = models.CASCADE)
    tsname = models.CharField(max_length=50)