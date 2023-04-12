from quiz_brain import QuizBrain
from question_model import Question
from data import question_data

question_bank = []
z = 0
for i in question_data:
    x = question_data[z]
    question = Question(x["question"], x["correct_answer"])
    question_bank.append(question)
    z += 1

quiz_machine = QuizBrain(question_bank)
continue_quiz = True
while continue_quiz:
    quiz_machine.next_question()
    print(f"Your current score is: {quiz_machine.score}\n")
    if not quiz_machine.still_has_questions():
        continue_quiz = False



print(f"You have completed the quiz!"
      f"Your final score was {quiz_machine.score} out of {len(quiz_machine.question_list)}")