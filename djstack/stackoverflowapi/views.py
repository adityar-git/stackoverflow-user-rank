from django.http import JsonResponse
from rest_framework import viewsets
from .models import User
from .serializer import UserSerializer
from stackapi import StackAPI, StackAPIError
import json
import pandas as pd


# Create your views here.
def index(request):
    print('Recieved URL:',request.GET['url'])

    user = user_rank(request.GET['url'])
    print('Sending...', user)
    return JsonResponse(user)


def user_rank(user_url):
    try:
        url = user_url
        user_option_file = 'stackoverflowapi\\options\\user-options.json'
        parse_web_name = 'stackoverflow'
        user_id = url.split('/')[4]

        SITE = StackAPI(parse_web_name)
        user_details = SITE.fetch('users/'+user_id)
        items = user_details['items'][0]

        selected_options = dict()
        user_options = dict(json.load(open(user_option_file)))
        for key in user_options.keys():
            if user_options[key] == 1:
                selected_options[key] = items[key]

        calculated_rank = rank_calculator(selected_options['reputation'])

        user_data_json = {
            "user_details": [selected_options],
            "Rank": calculated_rank
        }

        return user_data_json
    except StackAPIError as e:
        print(e.message)


def rank_calculator(user_reputation):
    scrape_file = 'stackoverflowapi\\scrape-file\\QueryResults.csv'
    scrape_file_handler = open(scrape_file, 'r', encoding='utf-8')
    contents = pd.read_csv(scrape_file_handler, sep=',')
    rank = len(contents[contents.reputation < user_reputation])*100/len(contents)
    scrape_file_handler.close()
    return rank


class UserAPI(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
