markov.py - a simple markov chain generator
===========================================

Inspired by greats such as [The Doom That Came To
Puppet](http://thedoomthatcametopuppet.tumblr.com/) and [Erowid
Recruiter](https://twitter.com/erowidrecruiter), this ultra-basic utility
reads plaintext files and uses them to train a [Markov
Chain](http://en.wikipedia.org/wiki/Markov_chain) and output a single
sentence.

This script fetches web content in addition to reading local files, but please
be considerate: If you're going to use a file many times then download it and
use your local copy.

    $ curl -o odyssey.txt http://classics.mit.edu/Homer/odyssey.mb.txt
    $ curl -o leavesofgrass.html https://www.gutenberg.org/files/1322/1322-h/1322-h.htm
    $ ./markov.py odyssey.txt leavesofgrass.html
    Having pried through the regions infinite, Whose air I breathe, whose
    ripples hear, lave me all that is the lord of thunder, who takes you to
    Ithaca?
