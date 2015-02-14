# chatparse

Usage:
<pre>
    ./chatparse.py - run the 4 test strings given
    ./chatparse.py "a sample message @greg" - dump the json for the string given
    ./giventests.py - run a test suite of given tests
    ./cornertests.py - run tests suite of some corner cases (that pass)
    ./failingtests.py - run tests that fail (left that wat for time consideration)
</pre>

Directions:

Please write, in your preferred language, code that takes a chat message string and returns a JSON string containing information about its contents. Special content to look for includes:
 
1. @mentions - A way to mention a user. Always starts with an '@' and ends when hitting a non-word character. (http://help.hipchat.com/knowledgebase/articles/64429-how-do-mentions-work-)
 
2. Emoticons - For this exercise, you only need to consider 'custom' emoticons which are ASCII strings, no longer than 15 characters, contained in parenthesis. You can assume that anything matching this format is an emoticon. (http://hipchat-emoticons.nyh.name)
 
3. Links - Any URLs contained in the message, along with the page's title.
 
For example, calling your function with the following inputs should result in the corresponding return values.
Input: "@chris you around?"
Return (string):
{
  "mentions": [
    "chris"
  ]
}
 
 
Input: "Good morning! (megusta) (coffee)"
Return (string):
{
  "emoticons": [
    "megusta",
    "coffee"
  ]
}
 
 
Input: "Olympics are starting soon; http://www.nbcolympics.com"
Return (string):
{
  "links": [
    {
      "url": "http://www.nbcolympics.com",
      "title": "NBC Olympics | 2014 NBC Olympics in Sochi Russia"
    }
  ]
}
 
 
Input: "@bob @john (success) such a cool feature; https://twitter.com/jdorfman/status/430511497475670016"
Return (string):
{
  "mentions": [
    "bob",
    "john"
  ],
  "emoticons": [
    "success"
  ]
  "links": [
    {
      "url": "https://twitter.com/jdorfman/status/430511497475670016",
      "title": "Twitter / jdorfman: nice @littlebigdetail from ..."
    }
  ]
}
 
 
There is no enforced time limit on this exercise.  Work on it until you're satisfied and feel it represents the quality of work you care to show off. Please take your time to make sure it is quality code. If this goes well the final step is an onsite interview!
 
Please create your project as a git repository that can be publicly viewed either on bitbucket.org or github.com and send the link to your repository for us to review.  
 
Cheers!
