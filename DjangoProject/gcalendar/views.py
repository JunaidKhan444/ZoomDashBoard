import os
from django.shortcuts import render, redirect
from django.http import HttpResponse
import google.oauth2.credentials
import google_auth_oauthlib.flow
import json, requests
from dotenv import load_dotenv, find_dotenv

# Create your views here.

#load_dotenv(find_dotenv())

#import os
#os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'


"""json_data = open('/home/moyeen/Desktop/client_secret.json')
json_obj = json.load(json_data)
#print(json_obj)
clientID = json_obj['web']['client_id']
clientSecret = json_obj['web']['client_secret']
projectID = json_obj['web']['project_id']
authURI = json_obj['web']['auth_uri']
tokenURI = json_obj['web']['token_uri']
redirectURI_1 = json_obj['web']['redirect_uris'][0]
#print(redirectURI_2)"""

def auth(request):
    """response = requests.get(tokenURI + "?client_id=" + clientID + "&client_secret=" + clientSecret)
    #var = json.loads(response.text)
    print(response.content)
    print(response.status_code)
    #print(response.content)

    return HttpResponse("done")"""

    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        '/home/moyeen/Desktop/client_secret.json',
        scopes=['https://www.googleapis.com/auth/calendar'])

    flow.redirect_uri = "https://57c3-103-249-211-178.ngrok.io"

    authorization_url, state = flow.authorization_url(access_type='offline', include_granted_scopes='true')
    print("authURL= ", authorization_url + "state= ", state)
    #print(type(authorization_url), type(state))

    return redirect(authorization_url)

def get_token(request):
    #print(request.session)
    state = request.GET.get('state')
    #print(state)
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        '/home/moyeen/Desktop/client_secret.json',
        scopes=['https://www.googleapis.com/auth/calendar'],
        state=state)
    #flow.redirect_uri = .url_for('oauth2callback', _external=True)
    authorization_response = request.get_full_path()
    #print("reqURL= ", authorization_response)
    flow.fetch_token(authorization_response=authorization_response)

    credentials = flow.credentials
    request.session['credentials'] = {
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': credentials.scopes}

    return HttpResponse("Access Token Obtained")