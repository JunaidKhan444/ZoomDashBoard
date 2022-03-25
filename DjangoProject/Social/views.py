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
        
        exchange_token = 'EAAHst9r8iOQBAP3ZA1ZA3ZBgSmxoVdwmj38hw3d5leAdgZACRpPvRqWU9PQa2AZASHDwZAomAvxTy1YQZBu61GKmdsXp15bXYu2ncM4m3ZCTOfpxrKp8mE6zdCEpLZB6yikqu1IfAIBKucqm9uzFKV00735DTWMkL76nhiZBZAirtSeUpPlA77tLPaAGY7ZBjLvMlX14Mi2f1eEOX1SP1qzF5gRZCzMykimV2GIcZD'
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
            obj,created1 = FacebookPosts.objects.get_or_create(post_id=datum['id'])
            if created1 == True:
                obj.post_id = datum['id']
                obj.post_data = datum['message']
                obj.post_date = datum['created_time']
                obj.save()

        
        """for x in records:
            print(x.post_data)"""
        
        return render(request,'Social/fb_table.html',{ 'event_list' : FacebookPosts.objects.all() })

