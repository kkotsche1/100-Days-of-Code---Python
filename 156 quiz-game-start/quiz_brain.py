class QuizBrain:

    def __init__(self, q_list):
        self.score = 0
        self.question_number = 0
        self.question_list = q_list

    def still_has_questions(self):
        number_of_questions = len(self.question_list)
        if self.question_number > number_of_questions-1:
            print("No more Questions!")
            return False
        else:
            return True


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False):")
        if user_answer == current_question.answer:
            print(f"Correct")
            self.score += 1
            return True
        else:
            print("Incorrect")
            return False



