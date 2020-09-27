#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import os
import sys
import unittest

import exercice


class TestExercice(unittest.TestCase):
    def test_prefixes(self):
        output = exercice.use_prefixes()
        answer = ["Jack", "Kack", "Lack", "Mack", "Nack", "Oack", "Pack", "Qack"]

        self.assertListEqual(
            output,
            answer,
            'Mauvaise identification de la parité de la longueur de la chaine'
        )

    def test_summation(self):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
            59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131,
            137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
            211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281,
            283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373,
            379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457,
            461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541]
        
        answer = sum(primes)
        output = exercice.prime_integer_summation()

        self.assertEqual(
            output,
            answer,
            'Retrait du mauvais caractère'
        )

    def test_factorial(self):
        values = [1, 3, 8, 10]

        output = [exercice.factorial(v) for v in values]
        answer = [math.factorial(v) for v in values]

        self.assertListEqual(
            output,
            answer,
            'Erreur dans le remplacement de caractère'
        )


if __name__ == '__main__':
    if not os.path.exists('logs'):
        os.mkdir('logs')
    with open('logs/tests_results.txt', 'w') as f:
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(sys.modules[__name__])
        unittest.TextTestRunner(f, verbosity=2).run(suite)