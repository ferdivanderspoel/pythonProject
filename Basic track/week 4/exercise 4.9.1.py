import turtle

def draw_square(animal, size):
    for _ in range(4):
        animal.color('pink')
        animal.forward(size)
        animal.left(90)
    animal.penup()
    animal.forward(size * 2)
    animal.pendown()

window = turtle.Screen()
window.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.pensize(3)

for _ in range(5):
    draw_square(tess, 20)
    tess.speed(10)

window.mainloop()