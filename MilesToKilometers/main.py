from tkinter import *
from playground import convert_m_km


window = Tk()
window.title("Miles to Kilometers")
window.minsize(width=200, height=100)
window.config(padx=2, pady=20)

# Label

my_label_is_equal = Label(text="is equal to")
my_label_is_equal.grid(row=1, column=0)
my_label_is_equal.config(padx=20, pady=20)

label_miles = Label(text="Miles")
label_miles.grid(row=0, column=3)
label_miles.config(padx=20, pady=20)

label_kilometers = Label(text="Km")
label_kilometers.grid(row=1, column=3)
label_kilometers.config(padx=20, pady=20)

answer_label = Label(text=f"0")
answer_label.grid(row=1, column=1)
answer_label.config(padx=20, pady=20)

# Input

input = Entry(width = 30)
input.grid(row=0, column=1)



# Button

def button_clicked():
    miles = input.get()
    miles = int(miles)
    answer_label.config(text=f"{miles*1.609}")


button = Button(text="Calculate!", command=button_clicked)
button.grid(row=3, column=1)
button.config(padx=20, pady=20)




window.mainloop()