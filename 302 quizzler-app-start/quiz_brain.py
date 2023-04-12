import html
from data import get_questions
from question_model import Question

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None
        self.round_count = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        try:
            self.current_question = self.question_list[self.question_number]
            q_text = html.unescape(self.current_question.text)
            self.question_number += 1
            return f"Q.{self.question_number + self.round_count*10}: {q_text}"

        except IndexError:
            question_bank_raw = get_questions()
            question_bank = []

            for question in question_bank_raw:
                question_text = html.escape(question["question"])
                question_answer = html.escape(question["correct_answer"])
                new_question = Question(question_text, question_answer)
                question_bank.append(new_question)
            self.round_count += 1
            self.question_list = question_bank
            self.question_number = 0
            self.current_question = self.question_list[self.question_number]
            self.question_number += 1
            q_text = html.unescape(self.current_question.text)
            return f"Q.{self.question_number + self.round_count*10}: {q_text}"

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
