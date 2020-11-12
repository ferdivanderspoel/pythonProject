import turtle

screen = turtle.Screen()
screen.bgcolor("lightgreen")
fer = turtle.Turtle()
fer.color("purple")
fer.pensize(3)

def draw_star(t, size):
    t.left(36)
    for _ in range(5):
        t.forward(size)
        t.left(144)
    t.penup()
    t.forward(350)
    t.right(144)
    t.pendown()

for _ in range(5):
    draw_star(fer, 100)

screen.exitonclick()