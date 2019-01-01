#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import re
import sys


class Markov(object):
    def __init__(self):
        self.words = dict()
        self.first_words = list()

    def __add(self, word, followup):
        if word in self.words.keys():
            self.words[word].append(followup)
        else:
            self.words[word] = [followup]

    def add_sentence(self, sentence):
        splt_sentence = [i.lower() for i in sentence.split(" ")]
        self.first_words.extend([splt_sentence[0]])
        for i, word in enumerate(splt_sentence):
            if i + 1 > len(splt_sentence) - 1:
                self.__add(word, None)
            else:
                self.__add(word, splt_sentence[i + 1])

    def stats(self):
        for k, followups in self.words.items():
            print("{}:".format(k))
            for f in followups:
                print("\t{}".format(f))

    def rand_first_word(self):
        return random.choice(list(self.first_words))

    def rand_followup_for(self, word):
        if word not in self.words:
            return ""
        return random.choice(list(self.words[word]))

    def get(self, word):
        if word in self.words.keys():
            return self.words[word]
        return ""

    def gen_sentence(self):
        full_sentence = list()
        i = 0

        next_word = self.rand_first_word()
        full_sentence.append(next_word)
        while (next_word != None):
            next_word = self.rand_followup_for(next_word)
            full_sentence.append(next_word)

            i += 1
            # Avoid infinite loops
            if i > 64:
                break
        if None in full_sentence:
            full_sentence.remove(None)
        return " ".join(full_sentence)

    def __repr__(self):
        return "%s" % [(k, v) for k, v in self.words.items()]

def usage():
    print("usage: {}: [stats | generate_number_of_sentences ] [filename]".format(sys.argv[0]))
    sys.exit(1)

if __name__ == '__main__':
    stats = False

    # TODO use argparse
    if len(sys.argv) == 3:
        if "stats" == sys.argv[1]:
            stats = True
        else:
            n = int(sys.argv[1])
    elif len(sys.argv) == 2:
        n = 1
    else:
        print("ERROR: missing filename")
        usage()

    m = Markov()
    with open(sys.argv[len(sys.argv) - 1], "r") as f:
        for line in f:
            l = line.replace("\n", "")
            if l == "":
                continue
            m.add_sentence(l)

    if stats:
        m.stats()
        sys.exit(0)

    for i in range(n):
        sentence = m.gen_sentence()
        while len(sentence.split(" ")) < 3:
            sentence = m.gen_sentence()
        print("{}{}\n".format(sentence[0].capitalize(), sentence[1:]))

