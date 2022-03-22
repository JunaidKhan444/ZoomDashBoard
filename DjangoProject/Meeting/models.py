from django.db import models
import uuid

# Create your models here.
class ZoomMeetings(models.Model):
    object_id = models.BigIntegerField(unique=True)
    meeting_topic = models.CharField(max_length=1000)
    meeting_starttime = models.DateTimeField(null=True)
    meeting_duration  =  models.IntegerField(null=True)
    meeting_created   = models.DateTimeField(null=True)
    meeting_url =  models.CharField(max_length=1000)
    
