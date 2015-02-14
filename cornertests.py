#!/usr/bin/env python3

import chatparse
import unittest

class CornerTests(unittest.TestCase):
    def test_userurl(self):
        '''test for @user in url'''
        msg = "http://user@example.com"
        expect = {
          "links": [
            {
              "url": msg,
              "title": None,
            }
          ]
        }
        result = chatparse.parse(msg)
        self.assertEqual(expect, result)

    def test_longemoticon(self):
        '''test for emoticon bigger that 15 chars'''
        msg = "(1234567890123456)"
        expect = {}
        result = chatparse.parse(msg)
        self.assertEqual(expect, result)

if __name__ == '__main__':
    unittest.main()
