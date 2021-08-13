# Testing file for trivia lab
# By: Jacob Wolf

# =============================================================================
#  More-Than-You-Need-To-Know Lounge
# =============================================================================
# Welcome to the More-Than-You-Need-To-Know Lounge, a chill place for code that
# you don't need to understand.

# Thanks for stopping by, we hope you find something that catches your eye.
# But don't worry if this stuff doesn't make sense yet -- as long as we know
# how to use code, we don't have to understand everything about it.

# Of course, if you really like this place, stay a while. You can ask a
# teacher about it if you're interested.
#
# =============================================================================

import unittest
import sys, io
from collections import defaultdict
import random


from game import TriviaGame
from question import Question

class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = io.StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout

class PatchStdin(object):
    def __init__(self, value):
        self._value = value
        self._stdin = sys.stdin
    def __enter__(self):
        # Monkey-patch stdin
        sys.stdin = io.StringIO(self._value)
        return self
    def __exit__(self, typ, val, traceback):
        # Undo the monkey-patch
        sys.stdin = self._stdin

class TestTriviaLab(unittest.TestCase):

    def test_check_guess(self):
        """
        Test checking the implementation of the check_guess() function.
        """
        question = Question("Test", "correct", ["correct", "incorrect"])
        self.assertTrue(question.check_guess("correct"))
        self.assertFalse(question.check_guess("incorrect"))
        self.assertFalse(question.check_guess("not an option"))

    def test_random_choices(self):
        options = ["0", "1", "2", "3", "4"]
        question = Question("Test", "0", options.copy())
        choices0 = question.random_choices().copy()
        self.assertTrue(set(options) == set(choices0))
        randomizedTest = False
        for i in range(100):
            choices1 = question.random_choices()
            if choices0 != choices1:
                randomizedTest = True
                break
        self.assertTrue(randomizedTest)

    def test_play_game(self):
        game = TriviaGame("test.txt", "t")
        with Capturing() as output:
            with PatchStdin("C\nD\ncorrect"):
                game.play()
        self.assertEqual(game.score, 3)


unittest.main()
