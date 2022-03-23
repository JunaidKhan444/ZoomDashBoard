import email
from multiprocessing import context
from urllib import request
from django.shortcuts import render,redirect
import jwt
import datetime
from django.views import View
#from zoomus import ZoomClient
from django.http import HttpResponse
import requests
import json
from .models import ZoomMeetings
from .forms import EditForm

def addmeeting(request):
    form = EditForm()
    
    if request.method == "POST":
        form = EditForm(request.POST)
        if form.is_valid():
            
            topic = form.cleaned_data['Meeting_Topic']
            date = form.cleaned_data['Meeting_Start_Date']
            print(type(date))
            duration = form.cleaned_data['Duration']
            password = form.cleaned_data['Password']
            date = str(date.strftime("%Y-%m-%dT%H:%M:%SZ"))
            print(date)
            print(type(date))
            
            """date = datetime.datetime(2022,3,22,13,30).strftime("%Y-%m-%dT%H:%M:%SZ")"""
            obj = {'topic':topic,'start_time':date,'duration':duration, 'password':password}
            time_now = datetime.datetime.now()
            expiration_time = time_now+datetime.timedelta(seconds= 20)
            headers = {
                'alg':'HS256','type':'JWT'
            }
            payload ={"iss":"4FKmr8Q1Qg236ltRBrpQ5Q","exp": round(expiration_time.timestamp())
            }
            encoded_jwt = jwt.encode(payload, "LwDi44ZefFPEOrtXhiBvkvH0aE2wLZDTojZV", algorithm="HS256")
            header = {'authorization':"Bearer {}".format(encoded_jwt)}
            email='mrjunaid444@gmail.com'
            url_Cmeetings = 'https://api.zoom.us/v2/users/{}/meetings'.format(email)
            create_meeting = requests.post(url_Cmeetings,json=obj,headers=header)
            print(create_meeting.status_code)

            return redirect('meetings')

        else:
             print("Invalid Form")
             context ={'form':form}
             return render(request,'Meeting/edit.html',context)

            
    context ={'form':form}
    
    return render(request,'Meeting/edit.html',context)


def deletemeeting(request,pk):
    item1 = ZoomMeetings.objects.get(object_id=pk)
    print(type(pk))
    if request.method == "POST":
        time_now = datetime.datetime.now()
        expiration_time = time_now+datetime.timedelta(seconds= 20)
        headers = {
            'alg':'HS256','type':'JWT'
        }
        payload ={"iss":"4FKmr8Q1Qg236ltRBrpQ5Q","exp": round(expiration_time.timestamp())
        }
        encoded_jwt = jwt.encode(payload, "LwDi44ZefFPEOrtXhiBvkvH0aE2wLZDTojZV", algorithm="HS256")
        header = {'authorization':"Bearer {}".format(encoded_jwt)}
        dmeeting_url = "https://api.zoom.us/v2/meetings/{}".format(int(item1.object_id))
        dmeeting = requests.delete(dmeeting_url,headers=header)
        print(dmeeting.text)
        print(dmeeting.status_code)
        if dmeeting.status_code == 204:
            item1.delete()
            return redirect ('meetings')
    
    context ={'item':item1}
    return render(request,'Meeting/delete.html',context)

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
        # C = Create and L = List
        url_Lmeetings = 'https://api.zoom.us/v2/users/{}/meetings'.format(email)
        header = {'authorization':"Bearer {}".format(encoded_jwt)}
        list_meetings = requests.get(url_Lmeetings,headers=header)
        data = json.loads(list_meetings.text)
        for datum in data['meetings']:
            #print(datum['uuid'], type(datum['uuid']))
            obj,created1 = ZoomMeetings.objects.get_or_create(object_id=datum['id'])
            if created1 == True:
            #obj = ZoomMeetings()
                obj.object_id= datum['id']
                #print(type(datum['id']))
                obj.meeting_topic = datum['topic']
                obj.meeting_starttime = datum['start_time']
                obj.meeting_duration = datum['duration']
                obj.meeting_created = datum['created_at']
                obj.meeting_url  = datum['join_url']
                obj.save()
           
        return render(request,'Meeting/zm_table.html',{ 'event_list' : ZoomMeetings.objects.all() })




