 # Daunte King
 # 3/8/25
  # P2LAB1
  # Program will calculate the diameter, circumference, and area of a circle

PI = 3.14159
radius_of_circle = float(input('What is the radius of the circle?: '))

diameter = 2 * radius_of_circle
print(f'\nThe diameter of the circle is {diameter:.1f} \n')
      
circumference = 2 * PI * radius_of_circle 
print(f'The circumference of the circle is {circumference:.2f} \n')

area = PI * (radius_of_circle ** 2 )
print(f'The area of the circle is {area:.3f}')