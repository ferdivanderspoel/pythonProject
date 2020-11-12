import turtle

def draw_square(animal, size):
        animal.color('blue')
        animal.forward(size)
        animal.right(90)

window = turtle.Screen()
window.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.pensize(1)

size = 2
for i in range(100):
    draw_square(tess, size)
    size += 3
    tess.speed(10)

window.mainloop()