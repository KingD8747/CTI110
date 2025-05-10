#Daunte King
#3/16/2025
#P1HW2
#Putting grades in a list and pulling them

grades_list = [ ]
Module1 = float(input("Enter grade for Module 1: "))
Module2 = float(input("Enter grade for Module 2: "))
Module3 = float(input("Enter grade for Module 3: "))
Module4 = float(input("Enter grade for Module 4: "))
Module5 = float(input("Enter grade for Module 5: "))
Module6 = float(input("Enter grade for Module 6: "))

grades_list.append(Module1)
grades_list.append(Module2)
grades_list.append(Module3)
grades_list.append(Module4)
grades_list.append(Module5)
grades_list.append(Module6)

lg = min(grades_list)
hg = max(grades_list)
sum = sum(grades_list)
avg = Module1+Module2+Module3+Module5+Module6 / 6

print('------------Results------------')
print(f'Lowest Grade:   {lg:>6}')
print(f'Highest Grade:  {hg:>6}')
print(f'Sum of Grades:  {sum:>7}')
print(f'Average:  {avg:>13}')
print('-------------------------------')