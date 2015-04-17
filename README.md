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

    $ curl -o jane-eyre.html 'https://www.gutenberg.org/files/1260/1260-h/1260-h.htm'
    $ ./markov.py 'http://arkhamarchivist.com/?dl_id=6' -d lovecraft-complete-works.mdb -q
    $ ./markov.py jane-eyre.html lovecraft-complete-works.mdb
    Rochester’s fortune: I came to see his venerable friend and sole assistant
    since the circumstances attending my infernal union with a star; the
    lineaments of a peeress.
