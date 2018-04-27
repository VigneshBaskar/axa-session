# -*- coding: utf-8 -*-
# <nbformat>4</nbformat>

# <codecell>

class SentencesIteratorForWV(object):
    def __init__(self, sentences):
        self.sentences = sentences
    def __iter__(self):
        for sentence in self.sentences:
            yield sentence
