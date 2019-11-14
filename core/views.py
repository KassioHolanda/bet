from django.shortcuts import render
import json
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view

api_key = '4deb941222a36f24ae93273efae8c21c'
url = 'https://api.the-odds-api.com/v3/sports'


# Create your views here.
@api_view()
def get_sports(request):
    sports_response = requests.get(url, params={
        'api_key': api_key
    })

    sports_json = json.loads(sports_response.text)
    if sports_json['success']:
        return Response(sports_json['data'])
    else:
        msg = {'Error':'Erro'}
        return Response(msg)
