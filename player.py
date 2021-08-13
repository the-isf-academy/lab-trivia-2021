# player.py
# Author: Emma Brown
# ==================


class Player:
    """ Creates a Player object for use in the TriviaGame. Player includes a
    name, score, and buzzer, and button.
    """

    def __init__(self, name, button, buzzer,led):
        
        self.name = name
        self.score = 0
        self.buzzer = buzzer
        self.button = button
        self.led = led

    def add_score(self):
        self.score += 1

    def get_name(self):
        return self.name
    
    def get_buzzer(self):
        return self.buzzer

    def get_button(self):
        return self.button

    def get_led(self):
        return self.led

