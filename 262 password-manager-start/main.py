import pyperclip
from tkinter import *
from tkinter import messagebox
from random import randrange, choice
AVAILABLE_CHARACTERS = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3",
                        "4","5","6","7","8","9","0","!","$","%","&","/","(",")","=","?",":","A","B","C","D","E","F","G","H","I","J","k","L","M","N","O","P",
                        "Q","R","S","T","u","V","W","X","Y","Z"]

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password_entry.delete(0,END)
    password = ""
    password_length = randrange(10,15)
    i = 0
    while i < password_length:
        password += choice(AVAILABLE_CHARACTERS)
        i += 1
    password_entry.insert(END, f"{password}")
    pyperclip.copy(f"{password}")
    return password

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    correct_info = None
    website = get_website()
    password = get_password()
    user = get_email()

    if len(website)==0:
        messagebox.showinfo(message="Please enter a Website before Adding")

    if len(user)==0:
        messagebox.showinfo(message="Please enter a Username or Email before Adding")

    if len(password)==0:
        messagebox.showinfo(message="Please enter a Password before Adding")

    if len(website)!= 0 and len(user)!=0 and len(password)!= 0:
        correct_info = messagebox.askyesno(message=f" You have entered the following\n"
                                                    f"Website: {website}\n"
                                                    f"Username/Email: {user}\n"
                                                    f"Password: {password}\n"
                                                    f"Is this information correct?")

        if correct_info:

            with open("passwords.txt", mode="a") as password_file:
                password_file.write(f"Website: {website}   Username: {user}   Password: {password}\n")

    website_entry.delete(0,END)
    password_entry.delete(0,END)
    email_entry.delete(0,END)


def retreive_password():

    website = get_website()
    with open("passwords.txt") as password_file:
        password_list = password_file.readlines()
        print(password_list)

    for entry in password_list:
        if website in entry:
            print(entry)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Konstantin's Password Manager")
window.config(padx=50, pady=20)

canvas = Canvas(width=300, height=300)
logo = PhotoImage(file="logo.png")
canvas.create_image(175, 150, image=logo)
canvas.grid(row=0, column=1)

label1 = Label(text="Website:")
label1.grid(row=1, column=0)
label2 = Label(text="Email/Username:")
label2.grid(row=2, column=0)
label3 = Label(text="Password:")
label3.grid(row=3, column=0)

website_entry = Entry(width=30)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=50)
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=30)
password_entry.grid(column=1, row=3, columnspan=2)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", command=retreive_password)
search_button.grid(column=2, row=1)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)



# Get the Website entered by the user

def get_website():
    return website_entry.get()

# Get the email entered by the user

def get_email():
    return email_entry.get()

#Get the Password generated or enterd by the user

def get_password():
    return password_entry.get()








retreive_password()



window.mainloop()