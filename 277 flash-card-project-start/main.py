from tkinter import *
from random import choice
import time

# --------- CONSTANT & VARIABLE INIT --------------- #

word_on_canvas = None
language_on_canvas = None
spanish_w = None
english_w = None

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")


# ---------------- SETTING UP PANDAS FRAME ------------ #

import pandas as pd

try:
    word_df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    word_df = pd.read_csv("data/es_en.csv")
finally:
    word_dictionary = {

    }
    for (index, row) in word_df.iterrows():
        word_dictionary[row["Spanish"]] = row["English"]



# --------------------- CREATING UI ------------------- #

#Creating Individual Spanish Flashcard
from random import *

def spanish_word():
    canvas.delete("all")
    spanish_word, english_word = choice(list(word_dictionary.items()))
    canvas_flashcard_image = canvas.create_image(450, 300, image=flashcard_image1)
    language_on_canvas = canvas.create_text(450, 150, text="Spanish", font=LANGUAGE_FONT)
    word_on_canvas = canvas.create_text(450, 300, text=f"{spanish_word}", font=WORD_FONT)
    return spanish_word


def english_word(english_word):
    canvas_flashcard_image = canvas.create_image(450, 300, image=flashcard_image2)
    language_on_canvas = canvas.create_text(450, 150, text="English", font=LANGUAGE_FONT)
    word_on_canvas = canvas.create_text(450, 300, text=f"{english_word}", font=WORD_FONT)


def flash_sequence():
    global spanish_w
    global english_w
    spanish_w = spanish_word()
    english_w = word_dictionary[spanish_w]
    canvas.after(3000,english_word, english_w)



# -------------- Saving New State to CSV ------------------ #

def csv_file_update():
    global spanish_w
    del word_dictionary[spanish_w]
    new_save = pd.DataFrame(word_dictionary.items(), columns=["Spanish", "English"])
    new_save.to_csv("./data/words_to_learn.csv")

#Window Initialization

window = Tk()
window.title("Konstantin's Flashcard Program")
window.config(padx=50, pady=50)
window.config(bg=BACKGROUND_COLOR)

#Flashcard Initialization
flashcard_image1 = PhotoImage(file="images/card_front.png")
flashcard_image2 = PhotoImage(file="images/card_back.png")


canvas = Canvas(height=600, width=900, bg=BACKGROUND_COLOR)
canvas.config(highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


#Initializing Buttons
wrong_image = PhotoImage(file="images/wrong.png")
right_image = PhotoImage(file="images/right.png")

button_red = Button(image=wrong_image, highlightthickness=0,command=flash_sequence)
button_red.grid(column=0, row=1)

button_green = Button(image=right_image, highlightthickness=0, command=lambda: [csv_file_update(), flash_sequence()])
button_green.grid(column=1, row=1)

print(word_dictionary)

flash_sequence()



window.mainloop()