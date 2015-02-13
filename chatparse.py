#!/usr/bin/env python3

import re

re_mentions = re.compile('(?<=@)\w+')
re_emoticons = re.compile('\((\w+)\)')
re_urls = re.compile('(https?://[^\s]+)')

def parse(msg):
    contents = {}
    mentions = re_mentions.findall(msg)
    if mentions:
        contents['mentions'] = mentions
    emoticons = re_emoticons.findall(msg)
    if emoticons:
        contents['emoticons'] = emoticons
    urls = re_urls.findall(msg)
    if urls:
        contents['urls'] = urls
    return contents

if __name__ == '__main__':
    result = parse('@test@1 @greg @aaa (smile) http://stiehl.com https://stiehl.com')
    print(result)
