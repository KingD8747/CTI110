# Daunte King
 # 3/9/2025
 # P2LAB2
 # Creates a dictionary where the key and value pairs are stored


cars_mpg = {
    'Camaro' : 18.21,
    'Prius' : 52.36,
    'Model S' : 110,
    'Silverado' : 26
}

keys = cars_mpg.keys()
print(keys)

car = input("\nEnter a vehicle to see it's mpg: ")
print(f'\nThe', car, 'gets', cars_mpg[car], 'mpg')

miles = float(input('\nHow many miles will you drive the car? '))
gas_needed = miles / cars_mpg[car]

print(f'\n {gas_needed:.2f}', 'gallon(s) are needed to drive the', car, miles, 'miles' )