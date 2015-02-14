#!/usr/bin/env python3

import chatparse
import unittest

class FailingTests(unittest.TestCase):
    def test_userurl(self):
        '''test for user@ in url'''
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

    def test_decode_nonutf8(self):
        '''test web page with non-utf8 encoding'''
        msg = "http://stiehl.com"
        expect = {
            "links": [
                {
                    "title": "The Stiehl Home Page",
                    "url": "http://stiehl.com"
                }
            ]
        }
        result = chatparse.parse(msg)
        self.assertEqual(expect, result)

if __name__ == '__main__':
    unittest.main()
