# answer_length.py

class AnswerLengthEvaluator:
    def __init__(self, answer):
        self.answer = answer

    def __str__(self):
        return f"The length of the answer '{self.answer}' is {len(self.answer)} characters."