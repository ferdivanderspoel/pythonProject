import turtle

def draw_square(animal, size):
    for _ in range(4):
        animal.color('blue')
        animal.forward(size)
        animal.left(90)

window = turtle.Screen() # Set up the window and its attributes
window.bgcolor("lightgreen")

tess = turtle.Turtle() # Create tess and set some attributes
tess.pensize(2)

size = 80 # Size of the smallest square
for _ in range(18):
    draw_square(tess, size)
    tess.right(20) # and give her some turn
    tess.speed(10)

window.mainloop()