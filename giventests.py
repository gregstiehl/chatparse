#!/usr/bin/env python3

import chatparse
import unittest

class GivenTests(unittest.TestCase):
    def test_mentions(self):
        '''@mentions - A way to mention a user. Always starts with an '@' and ends when hitting a non-word character.'''
        msg = "@chris you around?"
        expect = {
          "mentions": [
            "chris"
          ]
        }
        result = chatparse.parse(msg)
        self.assertEqual(expect, result)

    def test_emoticons(self):
        '''Emoticons - For this exercise, you only need to consider 'custom' emoticons which are ASCII strings, no longer than 15 characters, contained in parenthesis. You can assume that anything matching this format is an emoticon. (http://hipchat-emoticons.nyh.name)'''
        msg = "Good morning! (megusta) (coffee)"
        expect = {
          "emoticons": [
            "megusta",
            "coffee"
          ]
        }
        result = chatparse.parse(msg)
        self.assertEqual(expect, result)

    def test_links(self):
        '''Links - Any URLs contained in the message, along with the page's title.'''
        msg = "Olympics are starting soon; http://www.nbcolympics.com"
        expect = {
          "links": [
            {
              "url": "http://www.nbcolympics.com",
              "title": "NBC Olympics | Home of the 2016 Olympic Games in Rio",
            }
          ]
        }
        result = chatparse.parse(msg)
        self.assertEqual(expect, result)

    def test_all(self):
        '''Mentions, Emoticons & Links - all in one message'''
        msg = "@bob @john (success) such a cool feature; https://twitter.com/jdorfman/status/430511497475670016"
        expect = {
          "mentions": [
            "bob",
            "john"
          ],
          "emoticons": [
            "success"
          ],
          "links": [
            {
              "url": "https://twitter.com/jdorfman/status/430511497475670016",
              "title": 'Justin Dorfman on Twitter: "nice @littlebigdetail from @HipChat (shows hex colors when pasted in chat). http://t.co/7cI6Gjy5pq"'
            }
          ]
        }
        result = chatparse.parse(msg)
        self.assertEqual(expect, result)

if __name__ == '__main__':
    unittest.main()
