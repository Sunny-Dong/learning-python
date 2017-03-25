# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 15:02:10 2017

@author: sunnyday
"""

import requests

r = requests.get('http://api.reddit.com/controversial?limit=5')
r.raise_for_status()
reddit_data = r.json()
print (reddit_data['data']['children'][1]['data'])