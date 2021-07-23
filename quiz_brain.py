class QuizBrain:

    def __init__(self, question_list) -> None:
        self.question_number = 1
        self.question_list = question_list
        self.score = 0

    def new_question(self):
        current_question = self.question_list[self.question_number - 1]
        anwer_options = current_question.incorrect_answers.copy()
        anwer_options.append(current_question.correct_answer)
        str_answer_options = ''
        for answer in set(anwer_options):
            str_answer_options += answer + ' / '

        
        user_answer = input("#{}. {}\n(options: {}): \n".format(
            self.question_number, current_question.question, str_answer_options))
        self.check_answer(user_answer, current_question.correct_answer)
        self.question_number += 1

    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            print("Yes, you are correct!")
            self.score += 1
            print("Current score: {}/{}\n".format(
                self.score, len(self.question_list)))
        else:
            print("Wrong answer.")
            print("Current score: {}/{}\n".format(
                self.score, len(self.question_list)))

    def greeting(self):
        print("\nWelcome to our quiz!")
        print("We have {} questions for you. Good Luck!".format(len(self.question_list)))
        print()
    
    def bye(self):
        print("----------------------------------------")
        print("Your total score is: {}/{}".format(self.score, len(self.question_list)))
        print("Have a nice day!\n")
