#!/usr/bin/env python3

import html
import json
import re
import sys
import urllib.request

# regex searches for parsing (in global space so they are only compiled once)
re_mentions = re.compile(r'(?<=^|(?<=[^a-zA-Z0-9-\.]))@([A-Za-z_]+[A-Za-z0-9_]+)')
re_emoticons = re.compile(r'\((\w{1,15})\)')
re_urls = re.compile(r'(https?://[^\s]+)')
re_title = re.compile(r'<title>(.*?)</title>', re.IGNORECASE|re.DOTALL)

def url_title(url):
    # letting urlopen be the URL validator
    try:
        with urllib.request.urlopen(url) as h:
            page = h.read()
    except:
        return None, None
    title = re_title.search(page.decode())
    if title:
        title = html.unescape(title.group(1))
    return url, title

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
    links = []
    for url in re_urls.findall(msg):
        url, title = url_title(url)
        if url:
            links.append({'url': url, 'title': title})
    if links:
        contents['links'] = links

    return contents

if __name__ == '__main__':
    if len(sys.argv) > 1:
        msg = sys.argv[1]
        print('Input:', msg)
        print('Return (string):\n', json.dumps(parse(msg), indent=2, sort_keys=True, separators=(',', ': ')))
        exit(0)
        
    msgs = [
        '@chris you around?',
        'Good morning! (megusta) (coffee)',
        'Olympics are starting soon; http://www.nbcolympics.com',
        '@bob @john (success) such a cool feature; https://twitter.com/jdorfman/status/430511497475670016',
    ]

    for msg in msgs:
        print('Input:', msg)
        print('Return (string):\n', json.dumps(parse(msg), indent=2, sort_keys=True, separators=(',', ': ')))

    exit(0)
