from django.shortcuts import render,redirect
import jwt
import datetime
from django.views import View
#from zoomus import ZoomClient
#from django.http import HttpResponse
import requests
import json
from .models import ZoomMeetings



class DisplayMeetings(View):
    def get(self,request):
        time_now = datetime.datetime.now()
        expiration_time = time_now+datetime.timedelta(seconds= 20)
        headers = {
            'alg':'HS256','type':'JWT'
        }
        payload ={"iss":"4FKmr8Q1Qg236ltRBrpQ5Q","exp": round(expiration_time.timestamp())
        }
        encoded_jwt = jwt.encode(payload, "LwDi44ZefFPEOrtXhiBvkvH0aE2wLZDTojZV", algorithm="HS256")
        email = "mrjunaid444@gmail.com"
        url_Cmeetings = 'https://api.zoom.us/v2/users/{}/meetings'.format(email)
        url_Lmeetings = 'https://api.zoom.us/v2/users/{}/meetings'.format(email)

        """date = datetime.datetime(2022,3,22,13,30).strftime("%Y-%m-%dT%H:%M:%SZ")
        obj = {'topic':'Test Meeting','starttime':date,'duration':30, 'password':'1234'}
        header = {'authorization':"Bearer {}".format(encoded_jwt)}
        create_meeting = requests.post(url,json=obj,headers=header)"""
        
        
        header = {'authorization':"Bearer {}".format(encoded_jwt)}
        list_meetings = requests.get(url_Cmeetings,headers=header)
        data = json.loads(list_meetings.text)
        for datum in data['meetings']:
            #print(datum['uuid'], type(datum['uuid']))
            #obj,created1 = ZoomMeetings.objects.get_or_create(object_id=datum['uuid'])
            #if created1 == True:
            obj = ZoomMeetings()
            #obj.object_id= datum['uuid']
            obj.meeting_topic = datum['topic']
            obj.meeting_starttime = datum['start_time']
            obj.meeting_duration = datum['duration']
            obj.meeting_created = datum['created_at']
            obj.meeting_url  = datum['join_url']
            obj.save()
    


           
        return render(request,'Meeting/zm_table.html',{ 'event_list' : ZoomMeetings.objects.all() })