# coding: UTF-8
from base64 import b64decode
from pprint import pprint

import boto3
import os
import json
import urllib.request
import requests
from bs4 import BeautifulSoup
import ssl
import certifi

# 正しいCA証明書パスを指定して、SSLコンテキストを設定
ssl._create_default_https_context = ssl.create_default_context(cafile=certifi.where())

def lambda_handler(event, context):
    WEB_HOOK_URL = os.environ["WEB_HOOK_URL"]
    url = "url"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    show_select = soup.select("#koenno")[0]

    if len(show_select.contents) == 7:
        if '21' in (show_select.contents[4].text):
            requests.post(WEB_HOOK_URL, data=json.dumps({
                # メッセージ
                "text": "<!channel> message",
            }))
        if '22' in (show_select.contents[6].text):
            requests.post(WEB_HOOK_URL, data=json.dumps({
                "text": "<!channel> message",
            }))

    if len(show_select.contents) == 5:
        if '21' in (show_select.contents[2].text):
            requests.post(WEB_HOOK_URL, data=json.dumps({
                "text": "<!channel> message",
            }))
        if '22' in (show_select.contents[4].text):
            requests.post(WEB_HOOK_URL, data=json.dumps({
                "text": "<!channel> message",
            }))

    if len(show_select.contents) == 3:
        if '22' in (show_select.contents[2].text):
            requests.post(WEB_HOOK_URL, data=json.dumps({
                "text": "<!channel> message",
            }))

lambda_handler(None, None)