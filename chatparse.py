#!/usr/bin/env python3

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
                title = title.group(1)
            good_urls.append({'url': link, 'title': title})
    if good_urls:
        contents['links'] = good_urls

    return contents

if __name__ == '__main__':
    result = parse('@test@1 @greg @aaa (smile) https://stiehl.com http://www.nbcolympics.com')
    print(result)
