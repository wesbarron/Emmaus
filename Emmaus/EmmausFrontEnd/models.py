from django.db import models

# Create your models here.
class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

class GatheringInformation(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    cluster = models.CharField(max_length=200)
    time = models.CharField(max_length=200)

class BoardMember(models.Model):
    board_position = models.CharField(max_length=200)
    member = models.CharField(max_length=200)
    year = models.CharField(max_length=200)

class Pilgrim(models.Model):
    pilgrim_name = models.CharField(max_length=200)
    walk_number = models.CharField(max_length=200)
    walk_group = models.CharField(max_length=200)