#!/usr/bin/env python3

import re

re_mentions = re.compile('(?<=@)\w+')

def parse(msg):
    contents = {}
    contents['mentions'] = re_mentions.findall(msg)
    return contents

if __name__ == '__main__':
    result = parse('@test@1 @greg @aaa')
    print(result)
