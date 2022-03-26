
from django.db import models
from django.forms import CharField, IntegerField

# Create your models here.
class FacebookPosts(models.Model):
    post_id = models.TextField()
    post_data = models.CharField(max_length=1000)
    post_date = models.DateTimeField(null=True)
    
    