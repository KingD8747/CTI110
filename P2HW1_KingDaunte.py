#Daunte King
#3/16/2025
#P1HW2
#Doing basic math to help with budgeting

print('This program calculates and display travel expenses\n')

print('Enter Budget:', end=' ')
Budget = int(input()) 

print('\nEnter your travel destination:', end=' ')
Destination = input()

print('\nHow much do you think you will spend on gas?', end=' ')
g = int(input())

print('\nApproximately, How much will you need for accommodation/hotel?', end=' ')
a = int(input())

print('\nLast, How much do you need for food?', end=' ')
f = int(input())

f_b = float(Budget)
f_g = float(g)
f_a = float(a)
f_f = float(f)

print('\n------------Travel Expenses------------')
print(f'Location: {Destination:>16}')
print(f'Initial Budget: {'$':>6}{f_b:.2f}')

print(f'Fuel: {'$':>16}{f_g:.2f}')
print(f'Accommodation: {'$':>7}{f_a:.2f}')
print(f'Food: {'$':>16}{f_f:.2f}')
print('---------------------------------------')

Expenses = g + a + f
r = Budget - Expenses
f_r = float(r)
print(f'\nRemaining Balance: {'$':>3}{f_r:.2f}')

