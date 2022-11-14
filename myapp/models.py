from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UsersType(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)

    USER_TYPE_CHOICES = (
      ("admin", 'Admin'),
      ("Mod", 'Moderator'),
      ("DU", 'Debater'),
     )

    user_type = models.CharField(choices=USER_TYPE_CHOICES,max_length=25)
    userstatus = models.BooleanField(default=True)

class DebateTopic(models.Model):
    topic_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    aduser = models.ForeignKey(User,related_name='UsID', on_delete = models.CASCADE)
    closestatus = models.BooleanField(default=False)

class Views(models.Model):
    view_id = models.AutoField(primary_key=True)
    topic = models.ForeignKey(DebateTopic, related_name='USID', on_delete = models.CASCADE)
    user = models.ManyToManyField(DebateTopic)
    description = models.CharField(max_length=100)

class Votes(models.Model):
    vote_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='USeID', on_delete = models.CASCADE)
    view = models.ForeignKey(Views, related_name='VID', on_delete = models.CASCADE)
    topic = models.ForeignKey(DebateTopic, related_name='ID',  on_delete = models.CASCADE)
    votestatus = models.BooleanField()

class DepateWinner(models.Model):
    dw_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,related_name='USEID', on_delete = models.CASCADE)
    topic = models.ForeignKey(DebateTopic,related_name='UID', on_delete = models.CASCADE)
    winstatus = models.BooleanField()

class TopicSuggest(models.Model):
    user = models.ForeignKey(User, related_name='UID',on_delete = models.CASCADE)
    tsname = models.CharField(max_length=50)