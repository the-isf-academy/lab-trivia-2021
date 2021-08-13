# question.py
# Author: Emma Brown
# ==================


class Question:
    """ Creates a Question object for use in the TriviaGame. Question include a
    string questionPrompt, a string answer, and a list of string choices.
    """

    def __init__(self, questionPrompt, answer, choices):
        
        self.questionPrompt = questionPrompt
        self.choices = choices
        self.answer = answer

        answer_index = self.choices.index(self.answer)
        self.answer_letter = chr(65+answer_index)

    def check_guess(self, guess):
        """ Given a string guess, return True if the guess matches the answer to the question
        and False if it does not.
        """

        if len(guess) > 1:
            if guess.lower() == self.answer.lower():
                return True
            else:
                return False
        else:
            
           
            if guess.lower() == self.answer_letter.lower():
                return True
            else:
                return False


