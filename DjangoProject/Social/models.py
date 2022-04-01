
from django.db import models
from django.forms import CharField, IntegerField

# Create your models here.
class FacebookPosts(models.Model):
    post_data = models.CharField(max_length=10000)
    post_date = models.DateTimeField()
    
class InstaData(models.Model):
    media_id = models.BigIntegerField()
    media_type = models.CharField(max_length=50)
    comments_count = models.IntegerField()
    like_count = models.IntegerField()
    comments = models.CharField(max_length=100)

    

"""class InstaComments(models.Model):
    media_id = models.ForeignKey(InstaData, on_delete=models.CASCADE)
    comments = models.CharField(max_length=100)"""

    