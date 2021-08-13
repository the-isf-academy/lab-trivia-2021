# view.py
# Author: Emma Brown
# ==================

from time import sleep

class TerminalView:
    """ Creates a TerminalView object which displays the TriviaGame in
        terminal.
    """

    def show_question(self,questionNum, question):
        """ Shows a given question as a give questionNumber
        """
        print("\nQuestion " + str(questionNum) + ": " + question)

    def show_score(self,score,total):
        """Shows the score based on a given score.
        """
        print("Score: " + str(score) + '/' + str(total))

    def show_fill_in_the_blank(self, answer):
        """Gets an open response for a trivia question and returns it.
        """
        guess = input("Guess: ")
        return guess

    def show_multiple_choice(self,choices):
        """ Shows a multiple choice for a trivia question with the given
        choices and return the user's choice.
        """
        letterNum = 65
        for i in range(len(choices)):
            print("   " + str(chr(letterNum+i))+ ") " + choices[i])

        guess = input("Guess: ")
        return guess

    def give_point(self,players):

        player_name = input("Player Name: ")
        return player_name

    def correctAnswer(self):
        print("-- Correct! --\n")

    def wrongAnswer(self):
        print("-- Incorrect! --\n")

    def endGame(self):
        print("\n--------------------------")
        print("--- Thanks for Playing ---")
        print("--------------------------")
        return

