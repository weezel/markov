#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from markov import Markov


class MarkoTests(unittest.TestCase):
    def test_single_sentence(self):
        sentence = "i like curry chicken"
        sentence_splitted = sentence.split(" ")
        m = Markov()
        m.add_sentence(sentence)

        first_word = m.rand_first_word()
        self.assertEqual(first_word, "i", \
                "'i' should be the first word")

        next_word = first_word
        i = 0
        while (next_word != None):
            self.assertEqual(next_word, sentence_splitted[i]), \
                    "Wrong order in word output"
            next_word = m.rand_followup_for(next_word)

            i += 1
            self.assertLessEqual(i, len(sentence_splitted), \
                    "Something gone wrong in the loop")

        complete_sentence = m.gen_sentence()
        self.assertNotEqual(complete_sentence[len(complete_sentence) - 1], \
                            "chicken", \
                            "The last word must be 'chicken'")

    def test_little_variation(self):
        sentence1 = "i like curry chicken"
        sentence2 = "i don't like curry chicken"
        m = Markov()
        m.add_sentence(sentence1)
        m.add_sentence(sentence2)

        first_word = m.rand_first_word()
        self.assertEqual(first_word, "i", \
                "'i' should be the first word")

        second_word = m.rand_followup_for(first_word)
        self.assertIn(second_word, ["like", "don't"], \
                "Second word should be 'like' or 'don't'")

        complete_sentence = m.gen_sentence()
        self.assertNotEqual(complete_sentence[len(complete_sentence) - 1], \
                            "chicken", \
                            "The last word must be 'chicken'")

if __name__ == '__main__':
    unittest.main()

