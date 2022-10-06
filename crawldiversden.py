# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 10:04:34 2021

@author: One
"""

import requests
import webbrowser

#This url can change based on if liveaquaria changes the format of the image names
url = 'https://www.liveaquaria.com/images/diversden/approved/lg-04'
webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))

#Change 06211 to match the relevant date ahead you want to look
#Often can only look for what is going to be uploaded today or tomorrow
for x in range(0,1000):
    if x < 10:
        urls = url +'06211-' + '00' + str(x) + '.jpg'
    elif x < 100:
        urls = url +'06211-' + '0' + str(x) + '.jpg'
    else:
        urls = url +'06211-' + str(x) + '.jpg'
    r = requests.get(urls)
    if x%100 == 0:
        print("Checkpoint ", x)
    if r.status_code == 404:
        pass
    else:
        print(urls)
        webbrowser.get('chrome').open(urls)

for x in range(0,1000):
    if x < 10:
        urls = url +'31211-' + '00' + str(x) + 't.jpg'
    elif x < 100:
        urls = url +'31211-' + '0' + str(x) + 't.jpg'
    else:
        urls = url +'26211-' + str(x) + 't.jpg'
    r = requests.get(urls)
    if x%100 == 0:
        print("Checkpoint ", x)
    if r.status_code == 404:
        pass
    else:
        print(urls)
        webbrowser.get('chrome').open(urls)

for x in range(0,1000):
    if x < 10:
        urls = url +'31211-' + '00' + str(x) + 'p.jpg'
    elif x < 100:
        urls = url +'31211-' + '0' + str(x) + 'p.jpg'
    else:
        urls = url +'31211-' + str(x) + 'p.jpg'
    r = requests.get(urls)
    if x%100 == 0:
        print("Checkpoint ", x)
    if r.status_code == 404:
        pass
    else:
        print(urls)
        webbrowser.get('chrome').open(urls)