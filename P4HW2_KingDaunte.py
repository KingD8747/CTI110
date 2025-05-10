#Daunte King
#4/19/2025
#P4HW2_Salary
#Calculates Salary for multiple users

#Get inputs
num_employees = 0
tot_pay = 0
t_reg_rate = 0
t_gross = 0

while True:
    employee = input("Enter employee's name or \"Done\" to terminate: ")
    if employee.lower() == "done":
        break
    hrs = float(input(f"How many hours did {employee} work?"))
    pay_rate = float(input(f"What is {employee}'s pay rate: "))

    #Calculations
    if hrs > 40:
        ot = hrs - 40
        ot_pay = ot * (pay_rate*1.5)
        reg_hrs = 40
    else:
        ot = 0
        ot_pay = 0
        reg_hrs = hrs
    
    reg_pay = reg_hrs * pay_rate
    gross = ot_pay + reg_pay
    #Display Employee and their hours/pay
    print ('------------------------------------')
    print (f'Employee name:   {employee}')
    print (f'\nHours Worked   Pay Rate   OverTime   OverTime Pay        RegHour Pay        Gross Pay')
    print ('---------------------------------------------------------------------------------------------')
    print(f'{hrs:<15.1f}{pay_rate:<11.1f}{ot:<11.1f}{ot_pay:<20.2f}{reg_pay:<10.2f}{gross:15.2f}')
    
    # Update totals
    num_employees += 1
    tot_pay += ot_pay
    t_reg_rate += reg_pay
    t_gross += gross

# Final summary
print(f"Total number of employees entered: {num_employees}")
print(f"Total amount paid for overtime: ${tot_pay:.2f}")
print(f"Total amount paid for regular hours: ${t_reg_rate:.2f}")
print(f"Total amount paid in gross: ${t_gross:.2f}")