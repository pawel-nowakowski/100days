class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def quiz(self):
        for question in self.question_list:
            self.question_number += 1

            # fixes found encoding errors found in api
            question.text = question.text.replace('&quot;', '"')
            question.text = question.text.replace('&#039;', '\'')
            question.text = question.text.replace('&eacute;', 'e')

            answer = input(f"Question {self.question_number}: {question.text} (True/False)?: ").lower()
            self.check_answer(answer, question.answer.lower())

    def check_answer(self, user_answer, question_answer):
        if user_answer == question_answer:
            print("That's correct.")
            self.score += 1
        else:
            print("Incorrect answer")
        print(f"The correct answer was: {question_answer}")
        print(f"Your current score is {self.score}/{self.question_number}.")


