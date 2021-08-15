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

    def give_point(self, players):
        for i in range(len(players)):
            print("   " + str(i) + ". " + players[i].get_name())

        player_correct = int(input("   > Which player answered correctly? (select num): "))
        players[player_correct].add_score()

    def correctAnswer(self):
        print("-- Correct! --\n")

    def wrongAnswer(self):
        print("-- Incorrect! --\n")

    def endGame(self, players):
        print("\n--------------------------")

        print("----- Final Score -----")
        for i in range(len(players)):
            print("   " + str(i) + ". " + players[i].get_name() + ": " + str(players[i].get_score()))


        print("--------------------------")
        print("--- Thanks for Playing ---")
        print("--------------------------")
        return

