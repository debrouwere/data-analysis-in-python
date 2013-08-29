# encoding: utf-8

import json
import requests
import time
import os
import sys

endpoint = "http://content.guardianapis.com/search"
defaults = {
    'page': 1, 
    'page-size': 50,
    'order-by': 'oldest', 
    'show-fields': 'all', 
    'show-tags': 'all', 
    'format': 'json', 
    }

def fetch(date, api_key=None):
    params = {
        'from-date': date, 
        'to-date': date,
    }
    params.update(defaults)

    print "Fetching articles for {date}".format(date=date)

    if api_key:
        params['api-key'] = api_key

    dest = 'data/{date}-articles.json'.format(date=date)

    if os.path.exists(dest):
        print "{dest} already exists, skipping".format(dest=dest)
        return

    articles = open(dest, 'w')

    loaded = False
    while not loaded:
        response = requests.get(endpoint, params=params)
        response = response.json()['response']
        print "Loaded page {currentPage} of {pages}".format(**response)
        for article in response['results']:
            serialization = json.dumps(article) + '\n'
            articles.write(serialization)

        if response['currentPage'] < response['pages']:
            params['page'] += 1
        else:
            loaded = True

        time.sleep(0.1)

    print "Fetched all articles."