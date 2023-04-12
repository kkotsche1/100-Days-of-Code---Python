##################### Extra Hard Starting Project ######################
my_email = "konstantin.kotschenreuther1@gmail.com"
# 1. Update the birthdays.csv

import pandas as pd
import smtplib

# ------------ Converting CSv -> df -> Dictionary ------------- #
birthdays_dataframe = pd.read_csv("birthdays.csv")
birthdays_dictionary = {

}
for (index,row) in birthdays_dataframe.iterrows():
    birthdays_dictionary[row["name"]] = [row["email"], row["year"], row["month"], row["day"]]


# Choosing a random letter template
def choose_letter():
    from random import randint

    letter_index = randint(0,2)
    if letter_index == 0:
        with open("./letter_templates/letter_1.txt") as template:
            letter_text = template.read()
            return letter_text
    if letter_index == 1:
        with open("./letter_templates/letter_2.txt") as template:
            letter_text = template.read()
            return letter_text
    if letter_index == 2:
        with open("./letter_templates/letter_3.txt") as template:
            letter_text = template.read()
            return letter_text

# 2. Check if today matches a birthday in the birthdays.csv

import datetime as dt
now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
letter_text = choose_letter()


for name in birthdays_dictionary:
    letter_text=choose_letter()
    if birthdays_dictionary[name][2] == month:
        if birthdays_dictionary[name][3] == day:
            print("hello")
            letter_text = letter_text.replace("[NAME]", name)
            # Send email
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password="Kotschi.123")
                connection.sendmail(from_addr=my_email, to_addrs=birthdays_dictionary[name][0],
                                        msg=f"Subject:Happy Birthday {name}\n\n {letter_text}")






# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




