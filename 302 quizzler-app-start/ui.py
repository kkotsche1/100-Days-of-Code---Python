import html

THEME_COLOR = "#375362"
FONT = ("Arial", 12, "italic")
from tkinter import *
from quiz_brain import QuizBrain
from tkinter import messagebox

class QuizInterface:

    def get_next_question(self):
        self.canvas.config(bg="white")
        q_text = self.quiz.next_question()
        q_text = html.unescape(q_text)
        self.canvas.itemconfig(self.question_text, text=q_text)


    def __init__(self, quizbrain: QuizBrain):
        self.window = Tk()
        self.window.title("Konstantin's Quiz Game")
        self.window.config(bg= THEME_COLOR, padx=20, pady=20)

        self.quiz = quizbrain
        self.canvas = Canvas()
        self.canvas.configure(height=250, width=300)
        self.question_text = self.canvas.create_text(150,125,text=f"hi", font=FONT, width=275)
        self.canvas.grid(row=1,column=0, columnspan=2)

        self.score_label = Label(text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.correct_image = PhotoImage(file="images/true.png")
        self.incorrect_image = PhotoImage(file="images/false.png")

        self.true_button = Button(image=self.correct_image,borderwidth=0, command=self.user_says_true)
        self.true_button.grid(column=1, row=2)

        self.false_button = Button(image=self.incorrect_image, borderwidth=0, command=self.user_says_false)
        self.false_button.grid(column=0, row=2)

        self.get_next_question()

        self.window.mainloop()

    def user_says_true(self):
        correct = self.quiz.check_answer("True")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if correct:
            self.canvas.config(bg="green")
            self.window.update()
        else:
            self.canvas.config(bg="red")
            self.window.update()
        self.window.after(1000,self.get_next_question())

    def user_says_false(self):
        correct = self.quiz.check_answer("False")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if correct:
            self.canvas.config(bg="green")
            self.window.update()
        else:
            self.canvas.config(bg="red")
            self.window.update()
        self.window.after(1000,self.get_next_question())
