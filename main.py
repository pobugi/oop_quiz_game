from questions_db import QuestionBank
from question_model import Question
from quiz_brain import QuizBrain


questions_bank = QuestionBank().get_questions()
question_objects = []

for question in questions_bank:
    question_model = Question(
        category=question['category'],
        correct_answer=question['correct_answer'],
        difficulty=question['difficulty'],
        incorrect_answers=question['incorrect_answers'],
        question=question['question']
    )
    question_objects.append(question_model)


new_quiz = QuizBrain(question_objects)

new_quiz.greeting()
while new_quiz.question_number <= len(question_objects):
    new_quiz.new_question()
new_quiz.bye()
