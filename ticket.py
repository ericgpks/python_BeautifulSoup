# coding: UTF-8
from base64 import b64decode
import boto3
import os
import json
import urllib.request
import requests
from bs4 import BeautifulSoup


def lambda_handler(event, context):
    url = "xxx"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    show_ttl = soup.select(".show_list_ttl")
    if len(show_ttl) != 0:
        WEB_HOOK_URL = os.environ["WEB_HOOK_URL"]
        requests.post(WEB_HOOK_URL, data=json.dumps({
            # メッセージ
            "text": "<!channel> message",
        }))
