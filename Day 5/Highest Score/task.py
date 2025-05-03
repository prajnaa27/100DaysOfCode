student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
# print(range(1, 10))


#using for loop traditional method
max=student_scores[0]

for i in range(1,len(student_scores)-1):
    print(i)
    if student_scores[i]>max:
        max=student_scores[i]
        print(f"Inside for loop max{max}")
print(max)

#using sort
student_scores.sort()
print(student_scores)
print(f"Max is {student_scores[-1]}")