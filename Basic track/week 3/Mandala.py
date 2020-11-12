import turtle

def draw_multicolor_square(animal, size):
    """Make animal draw a multi-color square of given size."""
    for color in ["red", "purple", "hotpink", "blue"]:
        animal.color(color)
        animal.forward(size)
        animal.left(90)

window = turtle.Screen() # Set up the window and its attributes
window.bgcolor("lightgreen")

tess = turtle.Turtle() # Create tess and set some attributes
tess.pensize(3)

size = 5 # Size of the smallest square
for _ in range(200):
    draw_multicolor_square(tess, size)
    size += 2  # Increase the size for next time
    tess.forward(5) # Move tess along a little
    tess.right(30) # and give her some turn
    tess.speed(0)

window.mainloop()