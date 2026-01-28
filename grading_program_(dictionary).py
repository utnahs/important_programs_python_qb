student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades={}
for i in student_scores:
    if student_scores[i] in range(91,101):
        student_grades[i]='Outstanding'
    elif student_scores[i] in range(81,91):
        student_grades[i]='Exceeds Expectations'
    elif student_scores[i] in range(71,81):
        student_grades[i]='Acceptable'
    else:
        student_scores[i] <= 70
        student_grades[i]='Fail'
print(student_grades)
