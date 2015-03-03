'''
Created on Mar 2, 2015

@author: buck
'''

import requests

MAX_REDIRECTS = 1000

def get(url, **kwargs):
    kwargs.setdefault('allow_redirects', False)
    for i in range(0, MAX_REDIRECTS):
        response = requests.get(url, **kwargs)
        if response.status_code == requests.codes.moved or \
           response.status_code == requests.codes.found:
            if 'Location' in response.headers:
                url = response.headers['Location']
                continue
            else:
                print "Error when reading the Location field from HTTP headers"
        return response
        