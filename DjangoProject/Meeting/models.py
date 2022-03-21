from django.db import models
import uuid

# Create your models here.
class ZoomMeetings(models.Model):
    #object_id = models.CharField(max_length=100,unique=True)
    meeting_topic = models.CharField(max_length=1000)
    meeting_starttime = models.DateTimeField()
    meeting_duration  =  models.IntegerField()
    meeting_created   = models.DateTimeField()
    meeting_url =  models.CharField(max_length=1000)
