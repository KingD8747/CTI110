import turtle           # Allows us to use turtles
wn = turtle.Screen()    # Creates a playground for turtles
s = turtle.Turtle()     # Create a turtle, assign to s
t = turtle.Turtle()

for c in range(3):       #Tells t where to move
    t.forward(80)
    t.left(120)

for i in range(4):     #Tells s where to move
    s.forward(50)
    s.left(90)

# end commands
wn.mainloop()
