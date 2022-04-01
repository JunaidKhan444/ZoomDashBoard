from email.utils import parsedate_to_datetime
from http.client import HTTPResponse
from django.utils.dateparse import parse_date
from django.views import View
from .models import FacebookPosts, InstaData
from django.shortcuts import render
import requests
import json

# Create your views here.
class DisplayPosts(View):
    def get(self,request):
        
        exchange_token = 'EAAHst9r8iOQBAKUwNZAqE2GXjgcOvle6VVwIJmeM5LTwwuSFGNi3Eg6R58ZA8DdBZATcJZBSxpiFHFHxbZCTfLkt69rTuZCzdP2MmkWkwReDZAgMXGxWEUMmZAGj9iHeAcEIk9itBRD0Ks5zjce9JRj4KdTFAOnqal0vDbFdwv5glnMWXJ18BXC9EYZCXGZB5sZANTd709aSqB30aOTPaDmlpHMfqrGSZBq1QfAZD'
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

class IgData(View):
    def get(self, request):
        base_url = "https://graph.facebook.com/v13.0"
        user_id = "100572015934463"
        accessToken = 'EAAEqyxbMPZBYBAOgxOlCpT4WmdiXGIkvl5EIyB17Xj1rGuIifSfNeoLrEhcL4E0oJG2Rz3HDx9kKzQtnT7SGjqhRC77Ez3eyYhHvGmg1GP79K1KLuopcFt2MrKHZAEyZCqN0YPikj9gLHggRYzHAfdBUH4n7ZBR34uxXdBJ53ZCUTOA9q3YwR17mqoAlW7mUgrflZCRxn2qEWP0FCfmrilRZBSx2VTLqzcZD'
        account_url=base_url+'/'+user_id+'/accounts?access_token='+accessToken

        #Fetch account data and grab page id from the data 

        account_data = requests.get(account_url).json()
        page_id = account_data['data'][0]['id']
        #print(account_data)
        #print(account_data['data'])
        #print(account_data['data'][0]['id'])
        #print(page_id)


        #data = requests.get("https://graph.facebook.com/v13.0/103393368969921/feed?access_token=EAAHst9r8iOQBAG6Y8qNnlISjbSTsrB6ZC3uw3rkAjdOhyBnbwkizKFZB6HEVCSeMXuO6UOw8AKm8JMp5KiWlb27xcoEamUizzaoooVdwdHCru2J256TZCizeeIZBPXUZA3xRlZB8MlJbZBPqsffHZCIie0PZBoKeGBbitpZCNgH2x6PPpOUaKxbfQT6gOFXBkI2hUUyvQVTaIbrTw2ZBAQIQR2W")
        page_insta_url = base_url+'/'+page_id+'?fields=instagram_business_account&access_token='+accessToken
        insta_data = requests.get(page_insta_url).json()
        insta_acc_id = insta_data['instagram_business_account']['id']
        #print(insta_acc_id)


        ig_url = base_url+'/'+insta_acc_id+'/media?access_token='+accessToken
        insta_media_data = requests.get(ig_url).json()
        #print(insta_media_data)

        insta_media_id =[]
        for i in insta_media_data['data']:
            insta_media_id.append(i['id'])
        #print(insta_media_id)

        media_details= []
        for i in insta_media_id:
            media_url = base_url+'/'+i+'?fields=id,media_type,comments_count,like_count'+'&access_token='+accessToken
            res = requests.get(media_url).json()
            media_details.append(res)
        #print(media_details)

        comments = []
        for i in range(len(insta_media_id)):
            comments_url = "https://graph.facebook.com/v13.0/"+insta_media_id[i]+"/comments?access_token="+accessToken
            res5 = requests.get(comments_url).json()
            comms=[]
            for i in range(len(insta_media_id)):
                comms.append(res5['data'][i]['text'])
            comments.append(comms)
            #print(res5)
        #print(comments)
        #print(comments_url)

        #data = {
        media_id= []
        media_type=[]
        comments_count= []
        like_count= []

        #}
        for i in range(len(media_details)):
            media_id.append(media_details[i]['id'])
            media_type.append(media_details[i]['media_type'])
            comments_count.append(media_details[i]['comments_count'])
            like_count.append(media_details[i]['like_count'])
        for i in range(len(media_id)):
            for j in range(len(comments)):
            
                obj1 = InstaData()
                
                obj1.media_id = media_id[i]
                obj1.media_type = media_type[i]
                obj1.comments_count = comments_count[i]
                obj1.like_count= like_count[i]
                obj1.comments = comments[i][j]
                obj1.save()
        """for i in range(len(media_id)):
            obj2 = InstaComments()
            obj2.media_id=media_id[i]
            for j in range(len(comments)):
                obj2.comments = comments[i][j]"""
        #return HTTPResponse('Hello world')
        return render(request,'Social/instaTable.html', { 'event_list' : InstaData.objects.all() })
#