import turtle           # Allows us to use turtles
wn = turtle.Screen()    # Creates a playground for turtles
s = turtle.Turtle()     # Create a turtle, assign to s
t = turtle.Turtle()

t.forward(80)           #Tells t where to move
t.left(120)
t.forward(80)
t.left(120)
t.forward(80)
t.left(120)

s.forward(50)           #Tells S where to move
s.left(90)
s.forward(50)
s.left(90)
s.forward(50)
s.left(90)
s.forward(50)

# end commands
wn.mainloop()
