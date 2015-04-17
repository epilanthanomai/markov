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
    def __init__(self):
        self.wordmap = defaultdict(list)

    def append(self, a, b, c):
        self.wordmap[a, b].append(c)

    def next_word(self, a, b):
        choices = self.wordmap[a, b]
        return random.choice(choices)


class PlaintextSource(object):
    SENTENCE_ENDS = '!.?'

    def __init__(self, text):
        self.text = text

    def triples(self):
        words = self.text.split()
        for t in self.triples_from_words(words):
            yield t

    def triples_from_words(self, words):
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


class TextSource(object):
    def __init__(self, text, fragment=None):
        soup = BeautifulSoup(text)
        node = soup

        if fragment:
            node = soup.find(id=fragment)
        else:
            body = soup.find('body')
            if body:
                node = body

        self.text = unicode(node.text)

    def triples(self):
        psource = PlaintextSource(self.text)
        for t in psource.triples():
            yield t


class PdfSource(object):
    def __init__(self, contents):
        sio = StringIO(contents)
        pdf = pyPdf.PdfFileReader(sio)
        self.text = ' '.join(page.extractText() for page in pdf.pages)

    def triples(self):
        psource = PlaintextSource(self.text)
        for t in psource.triples():
            yield t


def get_sentence(db):
    def sentence_words():
        a, b = None, None
        c = db.next_word(a, b)
        while c is not None:
            yield c
            a, b = b, c
            c = db.next_word(a, b)

    words = list(sentence_words())
    return ' '.join(words)


def load_path(db, path):
    basepath, fragment = urldefrag(path)

    with closing(urllib.urlopen(basepath)) as f:
        contents = f.read()

    try:
        source = PdfSource(contents)
        for a, b, c in source.triples():
            db.append(a, b, c)
        return
    except:
        pass

    source = TextSource(contents, fragment)
    for a, b, c in source.triples():
        db.append(a, b, c)


def main(argv):
    parser = argparse.ArgumentParser(
            description='Generate Markov chains from web texts.')
    parser.add_argument('sources', metavar='F', nargs='+',
            help='Files or URLs to load')
    args = parser.parse_args(argv[1:]) 

    db = Database()
    for path in args.sources:
        load_path(db, path)

    print get_sentence(db)


if __name__ == '__main__':
    import sys
    main(sys.argv)
