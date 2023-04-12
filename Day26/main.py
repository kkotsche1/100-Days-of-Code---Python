names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Frank"]
from random import randint
student_scores = {student:randint(0,100) for student in names}

passed_students = {student:score for (student,score) in student_scores.items() if score>60}
print(passed_students)