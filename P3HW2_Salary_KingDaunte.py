#Daunte King
#3/21/2025
#P3HW2_Salary
#Calculates Salary

#Get inputs
employee = input("Enter employee's name: ")
hrs = float(input('Enter number of hours worked: '))
pay_rate = float(input("Enter employee's pay rate: "))

#Calculations
if hrs > 40:
    ot = hrs - 40
else:
    ot = 0

if ot>=1:
    ot_pay = ot * (pay_rate * 1.5)
else:
    ot_pay = 0 
reg_pay = (hrs-ot) * pay_rate
gross = ot_pay + reg_pay

#Display Employee and their hours/pay
print ('------------------------------------')
print (f'Employee name:   {employee}')

print (f'\nHours Worked   Pay Rate   OverTime   OverTime Pay        RegHour Pay        Gross Pay')
print ('---------------------------------------------------------------------------------------------')

print(f'{hrs:<15.1f}{pay_rate:<11.1f}{ot:<11.1f}{ot_pay:<20.2f}{reg_pay:<10.2f}{gross:15.2f}')