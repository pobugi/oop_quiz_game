class Question:
    def __init__(self, category, correct_answer, 
    difficulty, incorrect_answers, question) -> None:
        self.category = category
        self.correct_answer = correct_answer
        self.difficulty = difficulty
        self.incorrect_answers = incorrect_answers
        self.question = question
