from question_model import questionModel
from data import question_data
from quiz_brain import QuizBrain
question_bank = []

for question in question_data:
    qa = questionModel(question['question'], question['correct_answer'])
    question_bank.append(qa)


qb = QuizBrain(question_bank)
qb.quiz()