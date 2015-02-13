#!/usr/bin/env python3

import html.parser
import json
import re
import urllib.request

re_mentions = re.compile('(?<=@)\w+')
re_emoticons = re.compile('\((\w+)\)')
re_urls = re.compile('(https?://[^\s]+)')
re_title = re.compile('<title>(.*?)</title>', re.IGNORECASE|re.DOTALL)

def parse(msg):
    contents = {}
    mentions = re_mentions.findall(msg)
    if mentions:
        contents['mentions'] = mentions
    emoticons = re_emoticons.findall(msg)
    if emoticons:
        contents['emoticons'] = emoticons
    urls = re_urls.findall(msg)
    good_urls = []
    for link in urls:
        try:
            with urllib.request.urlopen(link) as h:
                page = h.read()
        except:
            page = None
        if page:
            title = re_title.search(page.decode())
            if title:
                h = html.parser.HTMLParser()
                title = h.unescape(title.group(1))
            good_urls.append({'url': link, 'title': title})
    if good_urls:
        contents['links'] = good_urls

    return json.dumps(contents)

if __name__ == '__main__':
    msgs = [
        '@chris you around?',
        'Good morning! (megusta) (coffee)',
        'Olympics are starting soon; http://www.nbcolympics.com',
        '@bob @john (success) such a cool feature; https://twitter.com/jdorfman/status/430511497475670016',
    ]

    for msg in msgs:
        print('Input:', msg)
        print('Return (string):\n', parse(msg))
