

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_df = pandas.DataFrame(alphabet)
alphabet_dictionary = {}
for index, row in alphabet_df.iterrows():
    alphabet_dictionary[row.letter] = row.code


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

continue_asking_user = True

while continue_asking_user:
    user_input = input("Please enter what you would like to have spelled out in NATO alphabet")
    user_input = user_input.upper()

    letter_list = [letter for letter in user_input]
    Nato_list = []
    try:
        for letter in letter_list:
            if letter != " ":
                Nato_list.append(alphabet_dictionary[letter])
            else:
                Nato_list.append(" ")


    except KeyError:
        print("Only letters of the alphabet and spaces are valid input")

    else:
        print(Nato_list)
