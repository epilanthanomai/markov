markov.py - a simple markov chain generator
===========================================

Inspired by greats such as [The Doom That Came To
Puppet](http://thedoomthatcametopuppet.tumblr.com/) and [Erowid
Recruiter](https://twitter.com/erowidrecruiter), this ultra-basic utility
reads plaintext files and uses them to train a [Markov
Chain](http://en.wikipedia.org/wiki/Markov_chain) and output a single
sentence.

Hopefully future versions will be more polite by caching parsed web files,
and more useful by ripping text out of markup.

    $ curl -o metamorphosis.txt https://www.gutenberg.org/cache/epub/5200/pg5200.txt
    $ curl -o frankenstein.txt https://www.gutenberg.org/cache/epub/84/pg84.txt
    $ curl -o grimms.txt http://www.gutenberg.org/cache/epub/2591/pg2591.txt
    $ ./markov.py metamorphosis.txt frankenstein.txt grimms.txt
    We saw Tilbury Fort and remembered the effect of solemnizing my mind
    upon these histories, whilst my friends were snatched away; I was
    oppressed by cold, I had departed.

