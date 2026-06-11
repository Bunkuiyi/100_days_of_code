# Grading Program
# You have access to a database of student_scores in the format of a dictionary.
# The keys in student_scores are the names of the students and the values are their exam scores.
#
# Write a program that converts their scores to grades.
#
#
#
# By the end of your program,
# You should have a new dictionary called student_grades that should contain student names as keys and their assessed grades for values.

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for students in student_scores:
    if 91 <= student_scores[students] <= 100:
        student_grades[students] = "Outstanding"
    elif 81 <= student_scores[students] <= 90:
        student_grades[students] = "Exceeds Expectations"
    elif 71 <= student_scores[students] <= 80:
        student_grades[students] = "Acceptable"
    else:
        student_grades[students] = "Fail"

print(student_grades)