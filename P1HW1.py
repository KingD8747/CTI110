#Daunte King
#3/1/25
#P1HW1
#Performing simple math equations. exponents, addition, and subtraction

print('-----Calculating Exponents----\n\n')


print('Enter an integer as the base value:', end=' ')
BaseValue = int(input())
print('Enter an integer as the exponent:', end=' ')
Exponent = int(input())
Answer = BaseValue * Exponent


print('\n\n',BaseValue, 'raised to the power of', Exponent,'is', Answer,'!!')


print('\n\n-----Addition and Subtraction----\n\n')


print('Enter a starting integer:', end=' ')
x = int(input())
print('Enter an integer to add:', end=' ')
y = int(input())
print('Enter an integer to subtract:', end=' ')
z = int(input())
N = x + y - z

print('\n\n',x,'+',y,'-',z,'is equal to',N)
