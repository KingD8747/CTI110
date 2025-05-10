#Daunte King   
#4/20/25
#P5LAB
#Self Checkout
import random

def disperse_change(change):
    change = change 
#converting Value to an integer
    if change == 0:
        print('No change')
        
    change = round(change * 100)


#Determine how many dollars are needed
    num_dollars = change // 100
    change = change - (num_dollars * 100)

    if num_dollars > 0:
        if num_dollars == 1:
            print(f'{num_dollars} Dollar')
    else:
            print(f'{num_dollars} Dollars')
#Determine how many Quarters are needed
    num_quarters = change // 25
    change = change - (num_quarters * 25)

    if num_quarters > 0:
        if num_quarters == 1:
            print(f'{num_quarters} Quarter')
    else:
            print(f'{num_quarters} Quarters')

#Determine how many Dimes are needed
    num_dimes = change // 10
    change = change - (num_dimes * 10)

    if num_dimes > 0:
        if num_dimes == 1:
            print(f'{num_dimes} Dime')
        else:
            print(f'{num_dimes} Dimes')

#Determine how many nickels are needed
    num_nickels = change // 5
    change = change - (num_nickels * 5)

    if num_nickels > 0:
        if num_nickels == 1:
            print(f'{num_nickels} Nickel')
        else:
            print(f'{num_nickels} Nickels')

#Determine how many pennies are needed
    num_pennies = change
    if num_pennies > 0:
        if num_pennies == 1:
            print(f'{num_pennies} Penny')
        else:
            print(f'{num_pennies} Pennies')

pay_owe = round(random.uniform(0.01, 100.00), 2)
print("You owe $",pay_owe)
cash = float(input('How much cash will you put in the self-checkout? $'))

change = cash - pay_owe
print(f"Change is {change:.2f}")

disperse_change(change)
