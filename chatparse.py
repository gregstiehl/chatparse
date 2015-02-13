#!/usr/bin/env python3

import html
import json
import re
import urllib.request

re_mentions = re.compile('(?<=@)\w+')
re_emoticons = re.compile('\((\w+)\)')
re_urls = re.compile('(https?://[^\s]+)')
re_title = re.compile('<title>(.*?)</title>', re.IGNORECASE|re.DOTALL)

def parse(msg):
    contents = {}
    # look for @user mentions
    mentions = re_mentions.findall(msg)
    if mentions:
        contents['mentions'] = mentions

    # look for (emoticon)
    emoticons = re_emoticons.findall(msg)
    if emoticons:
        contents['emoticons'] = emoticons

    # look for http://link.com and read page for title
    urls = re_urls.findall(msg)
    links = []
    for link in urls:
        try:
            with urllib.request.urlopen(link) as h:
                page = h.read()
        except:
            continue
        title = re_title.search(page.decode())
        if title:
            title = html.unescape(title.group(1))
        links.append({'url': link, 'title': title})
    if links:
        contents['links'] = links

    return contents

if __name__ == '__main__':
    msgs = [
        '@chris you around?',
        'Good morning! (megusta) (coffee)',
        'Olympics are starting soon; http://www.nbcolympics.com',
        '@bob @john (success) such a cool feature; https://twitter.com/jdorfman/status/430511497475670016',
    ]

    for msg in msgs:
        print('Input:', msg)
        print('Return (string):\n', json.dumps(parse(msg), indent=2, separators=(',', ': ')))
