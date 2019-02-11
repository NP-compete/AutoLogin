#!/usr/bin/env python
# coding=utf-8
import os
os.system('pip install lxml bs4 requests')

import signal
import sys
import time

import requests
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = 'https://192.168.56.2:8090/httpclient.html'

def signal_handler(signal, frame):
    logoff()
    sys.exit(0)


def login():
    payload = {
        'mode': '191',
        'username': username,
        'password': password
    }
    with requests.Session() as s:
        p = s.post(url, data=payload, verify=False)
        soup = BeautifulSoup(p.text, "xml")
        for i in soup.find_all('message'):
            response = i.text
            print(username + ": " + response)
    return response


def logoff():
    payload = {'mode': 193, 'username': username}
    with requests.Session() as n:
        j = n.post(url, data=payload, verify=False)
        soup = BeautifulSoup(j.text, "xml")
        for i in soup.find_all('message'):
            response = i.text
            print(username + ": " + response)


if __name__ == "__main__":
#    username = input('Enter username:\n')
#    password = input('Enter password:\n')
    username = ' input username here'
    password = ' input password here'
    signal.signal(signal.SIGINT, signal_handler)
    result = login()

    while result == 'You have successfully logged in':
        time.sleep(7100)
        result = login()
