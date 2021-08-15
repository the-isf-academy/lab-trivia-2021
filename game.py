# game.py
# Author: Emma Brown
# ==================

import random
from view import TerminalView
from question import Question
from time import sleep
from player import Player
from gpiozero import LED, Button, TonalBuzzer
from signal import pause
from gpiozero.tones import Tone


class TriviaGame:

    def __init__(self, triviaFile,player_list):
        """ Creates a TriviaGame objects using string TriviaFile as the path to the txt file of
        questions.
        """
        self.triviaQuestions = []
        self.players = player_list
        self.score = 0
        self.questionNum = 0
        self.guess = ""

        self.view = TerminalView()

        self.triviaQuestionsInit(triviaFile)

    def play(self):
        """ Plays the trivia game (or at least one round of it)/
        """

        for prompt in self.triviaQuestions:
            self.view.show_question(self.questionNum,prompt.questionPrompt)

            guessed = False

            while guessed == False:
                if self.players[0].get_button().is_pressed:
                    # self.players[0].get_buzzer().play(Tone(60))
                    # sleep(1)
                    # self.players[0].get_buzzer().stop()

                    if guessed == False:
                        guessed = True
                        self.players[0].get_led().on()
                        sleep(1)
                        self.players[0].get_led().off()

                elif self.players[1].get_button().is_pressed:
                        # self.players[1].get_buzzer().play(Tone(60))                                             
                        # sleep(1)
                        # self.players[1].get_buzzer().stop()                                                     
                                                                                        
                        if guessed == False:                                                  
                            guessed = True
                            self.players[1].get_led().on()
                            sleep(1)
                            self.players[1].get_led().off() 

            self.view.give_point(self.players)



            # if len(prompt.choices)>1:
            #     self.guess = self.view.show_multiple_choice(prompt.choices)
            # else:
            #     self.guess = self.view.show_fill_in_the_blank(prompt.answer)


            # if prompt.check_guess(self.guess) == True:
            #     self.score += 1
            #     self.view.correctAnswer()
            # else:
            #     self.view.wrongAnswer()

            # self.questionNum += 1

            # self.view.show_score(self.score,self.questionNum)
        self.view.endGame()

    def triviaQuestionsInit(self,triviaFile):
        """ Reads the trivia questions file from the path triviaFile and adds Question objects to the
        game's list of questions.
        """
        error = False
        questionPrompt = ""
        answer = []

        with open(triviaFile) as file:
            line = file.readline()

            while line:
                if line =="Question:\n":
                    line = file.readline()
                    questionPrompt = line.strip()

                elif line == "Choices:\n":
                    line = file.readline()
                    choices = list(line.strip().split(","))
                    answer = choices[0]
                    random.shuffle(choices)
                    self.triviaQuestions.append(Question(questionPrompt,answer,choices))

                elif line != "\n":
                    error = True

                line = file.readline()

        if error == True:
            print("Formatting of trivia.txt is incorrect. Some questions may not appear.")

        random.shuffle(self.triviaQuestions)

def set_up_game():
    print("---------------------------")
    print("--- Welcome to CS Triva ---")
    print("---------------------------")

    buttons = [Button(17),Button(6)]
    buzzers = [TonalBuzzer(27),TonalBuzzer(5)]
    leds = [LED(19),LED(13)]

    player_list = []
    for i in range(2):
        print("Enter Player",i,"name:")
        player_name = input("   ")
        player_list.append(Player(player_name,buttons[i],buzzers[i],leds[i]))

    triviaFile = "trivia.txt"
    game = TriviaGame(triviaFile,player_list)
    game.play()

if __name__ == "__main__":
    set_up_game()







