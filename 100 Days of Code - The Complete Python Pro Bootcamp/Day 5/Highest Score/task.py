student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

total_scores = sum(student_scores)

sum = 0
for score in student_scores:
    sum += score

print(sum)

print(max(student_scores))

max = 0
for highest_score in student_scores:
    if highest_score > max :
       max = highest_score


print(max)


