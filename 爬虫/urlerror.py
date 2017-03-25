# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 16:33:07 2017

@author: sunnyday
"""

import urllib

requset = urllib.request.Request('http://www.xxxxx.com')
try:
    urllib.request.urlopen(request,timeout=10)
except urllib.error.URLError as e:
    print (e.reason)
    
import urllib2

req = urllib2.Request('http://blog.csdn.net/cqcre')
try:
    urllib2.urlopen(req)
except urllib2.HTTPError, e:
    print e.code
except urllib2.URLError, e:  #URL是父类error应写道后面
    print e.reason
else:
    print "OK"    