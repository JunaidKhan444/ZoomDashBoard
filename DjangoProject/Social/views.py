from email.utils import parsedate_to_datetime
from django.utils.dateparse import parse_date
from django.views import View
from .models import FacebookPosts
from django.shortcuts import render
import requests
import json

# Create your views here.
class DisplayPosts(View):
    def get(self,request):
        
        exchange_token = 'EAAHst9r8iOQBAEfh5w8t62MclzdSMTtrTsZAHwThaYZAocgZCeMTDcXZA9lfTTu9I5hG7taSIi7g6BynwkLhHZBnlH4boNdsuVq9c5NC90qlf3bKakUeQVilxfZCWMiYV1RtgZAq8WAleAuhIQ7GjOGteXtnyMa7RDKr1AItUJmjZAHds1uwiEmt2LhRB67ROfeRB0ITBHMgldmDXbooaRHabvWwJZBMZBRKYZD'
        #template_name ='fb_table.html'
        response1 = requests.get("https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id=541749373864164&client_secret=0492ef6f4cc4f745b8dcc688cffd6cbd&fb_exchange_token={}".format(exchange_token))
        long_token1 = json.loads(response1.text)
        UserAccessToken = long_token1['access_token']
        page_id = 103393368969921
        response2 = requests.get("https://graph.facebook.com/{}?fields=access_token&access_token={}".format(page_id,UserAccessToken))
        long_token2 = json.loads(response2.text)
        PageAccessToken = long_token2['access_token']

        post_data = requests.get("https://graph.facebook.com/v13.0/{}/feed?access_token={}".format(page_id,PageAccessToken))
        rating = requests.get("https://graph.facebook.com/v13.0/{}/ratings?fields=review_text&access_token={}".format(page_id,PageAccessToken))
        data = json.loads(post_data.text)
        print(rating.text)
        for datum in data['data']:
            obj = FacebookPosts()
            obj.post_data = datum['message']
            obj.post_date = datum['created_time']
           
            obj.save()

        
        """for x in records:
            print(x.post_data)"""
        
        return render(request,'Social/fb_table.html',{ 'event_list' : FacebookPosts.objects.all() })

