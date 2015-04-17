#!/usr/bin/env python

import argparse
import random
import urllib
from collections import defaultdict
from contextlib import closing
from cStringIO import StringIO
from urlparse import urldefrag

import pyPdf
from bs4 import BeautifulSoup


class Database(object):
    SENTENCE_ENDS = '!.?'

    def __init__(self):
        self.wordmap = defaultdict(list)

    def load_text(self, path):
        basepath, fragment = urldefrag(path)
        with closing(urllib.urlopen(basepath)) as f:
            contents = f.read()

        try:
            self.load_from_pdf(contents)
        except:
            self.load_from_soup_string(contents, fragment)

    def load_from_pdf(self, contents):
        sio = StringIO(contents)
        pdf = pyPdf.PdfFileReader(sio)
        text = ' '.join(page.extractText() for page in pdf.pages)
        self.load_from_string(text)

    def load_from_soup_string(self, ss, fragment):
        soup = BeautifulSoup(ss)
        node = soup

        if fragment:
            node = soup.find(id=fragment)
        else:
            body = soup.find('body')
            if body:
                node = body

        self.load_from_string(unicode(node.text))

    def load_from_string(self, s):
        ts = self.triples_from_string(s)
        for a, b, c in ts:
            self.wordmap[a, b].append(c)

    def triples_from_string(self, s):
        words = s.split()
        for t in self.triples(words):
            yield t

    def triples(self, words):
        # We want chains for sentences. Use a (None, None) pair to represet
        # each sentence beginning and end.
        triple = [None, None, None]
        for word in words:
            triple = (triple + [word])[1:]
            yield triple
            if word[-1] in self.SENTENCE_ENDS:
                # We'll call this the end of a sentence. Probably.
                triple = (triple + [None])[1:]
                yield triple
                triple = (triple + [None])[1:]
                yield triple

    def sentence(self):
        words = list(self.sentence_words())
        return ' '.join(words)

    def sentence_words(self):
        a, b = None, None
        c = self.next_word(a, b)
        while c is not None:
            yield c
            a, b = b, c
            c = self.next_word(a, b)

    def next_word(self, a, b):
        choices = self.wordmap[a, b]
        return random.choice(choices)


def main(argv):
    parser = argparse.ArgumentParser(
            description='Generate Markov chains from web texts.')
    parser.add_argument('sources', metavar='F', nargs='+',
            help='Files or URLs to load')
    args = parser.parse_args(argv[1:]) 

    db = Database()
    for path in args.sources:
        db.load_text(path)
    print db.sentence()

if __name__ == '__main__':
    import sys
    main(sys.argv)
