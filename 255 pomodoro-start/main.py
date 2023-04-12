from tkinter import *
import time
from math import floor
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECK_MARK = "✔"
check_marks = ""
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rounds = 8
continue_counting = TRUE
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global check_marks
    check_marks = ""
    window.after_cancel(timer)
    global rounds
    rounds = 8
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text=f"00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global rounds
    global continue_counting
    if rounds > 0:
        if rounds == 1:
            timer_label.config(text="Long Break", fg=RED)
            continue_counting = TRUE
            count_down(LONG_BREAK_MIN)
        elif rounds % 2 == 0:
            timer_label.config(text="Work Time")
            continue_counting = TRUE
            count_down(WORK_MIN)
        else:
            timer_label.config(text="Short Break", fg=PINK)
            continue_counting = TRUE
            count_down(SHORT_BREAK_MIN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global check_marks
    global rounds
    global continue_counting
    global timer
    if continue_counting:
        minutes = floor(count/60)
        seconds = count % 60
        if minutes < 10:
            minutes = f"0{minutes}"
        if seconds < 10:
            seconds = f"0{seconds}"
        canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
        if count > 0:
            timer = window.after(1000, count_down, count-1)
        if count == 0:
            if rounds % 2 == 0:
                check_marks += CHECK_MARK
                check_mark_label = Label(text=f"{check_marks}", bg=YELLOW)
                check_mark_label.grid(column=1, row=2)
            rounds -= 1
            start_timer()



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Konstantin's Pomodoro")
window.config(padx=50, pady=20, bg=YELLOW)




canvas = Canvas(width=300, height=300, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(150, 140, image=tomato_image)
timer_text = canvas.create_text(150,160, text=f"00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1,column=1)

check_mark_label = Label(text=f"{check_marks}", bg=YELLOW)
check_mark_label.grid(column=1, row=2)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "bold"))
timer_label.grid(row=0, column=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2,column=0)

reset_button = Button (text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)








window.mainloop()
