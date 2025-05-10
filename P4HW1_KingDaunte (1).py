#Daunte King
#4/19/25
#P4HW1
#Collecting scores and giving a grade back

num_scores = int(input("How many scores do you want to enter?"))

scores = []

for s in range(num_scores):
    while True:
        score = int(input(f"Enter score #{s + 1}: "))
        if 0 <= score <= 100:
            scores.append(score)
            break
        else:
            print("INVALID Score entered!!!!")
            print("Score should be between 0 and 100")
            print(f"Enter score #{s+1} again: ", end ='')
            score = int(input())
        if 0 <= score <= 100:
            scores.append(score)
            break


low = min(scores)
scores.remove(low)
avg = sum(scores)/len(scores)

# determine letter grade for average


if avg >= 90:
    grade = 'A'
elif avg >= 80:
    grade = 'B'
elif avg >= 70:
    grade = 'C'
elif avg >= 60:
    grade = 'D'
else:
    grade = 'F'


print('------------Results------------')
print(f'Lowest Score  :   {low:.1f}')
print(f'Modified List :  {scores}')
print(f'Scores Average:  {avg:.2f}')
print(f"Grade         :  {grade}")
print('-------------------------------')
