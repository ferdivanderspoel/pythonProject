import turtle

screen = turtle.Screen()
fer = turtle.Turtle()

def draw_star(t, size):
    t.left(36)
    for _ in range(5):
        t.forward(size)
        t.left(144)

draw_star(fer, 100)

fer.hideturtle()

screen.exitonclick()