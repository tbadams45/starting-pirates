# starting-pirates
Here's a riddle for you: What seven letter word can you take away a single letter from and have it make a new word, repeating all the way down to one letter?

Spoiler alert:
1. Pirates
2. Pirate
3. Irate
4. Rate
5. Ate
6. At
7. A

Now - what eight letter word can you do the same thing? What about a nine letter word? A TEN letter word? I wanted to find out, so I made a python script that will tell us the answer. The foundation is the excellent [SCOWL word database](http://wordlist.aspell.net/), which gives us an easy reference to see if a word is in the dictionary. 

To run, clone or download the repository and run the aptly named script `run_me.py` on the command line using Python 3. You'll get a long list of words of different word lengths that fulfill this criteria. Most of them are "false positives" in the sense that the words that they use aren't words that most of us know (or words that maybe are *technically* words but don't feel legit). However, you will find this one:

1.  Splittings
2.  Splitting
3.  Spitting
4.  Sitting
5.  Siting
6.  Sting
7.  Sing
8.  Sin
9.  In
10. I
