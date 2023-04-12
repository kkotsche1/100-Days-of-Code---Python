from question_model import Question
from data import get_questions
from quiz_brain import QuizBrain
from ui import QuizInterface
import html

question_bank_raw = get_questions()
question_bank = []

for question in question_bank_raw:
    question_text = html.escape(question["question"])
    question_answer = html.escape(question["correct_answer"])
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)



quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)


